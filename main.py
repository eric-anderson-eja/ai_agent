import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import SYSTEM_PROMPT
from functions.call_function import available_functions, call_function


# *****   Configuration   *****
load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL_ID = 'gemini-2.5-flash'

if not API_KEY:
    print("Error: GEMINI_API_KEY not found in environment.")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)



# *****  Input Handling  *****
parser = argparse.ArgumentParser(description="ai_bot")
parser.add_argument("user_prompt", type=str, help="Please enter prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
user_prompt = args.user_prompt
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


# *****  Core Logic  *****
response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=SYSTEM_PROMPT)
    )

# *****  Validation and Output   *****
if response.usage_metadata == 'None':
    raise RuntimeError("POSSIBLE FAILED REQUEST, no token metadata")
if args.verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if not response.function_calls:
    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
else:
    function_results = []
    for function_call in response.function_calls:
        function_call_result = call_function(function_call, args.verbose)

        # 1) parts must exist
        if not function_call_result.parts:
            raise RuntimeError("Empty parts list from function call")

        part = function_call_result.parts[0]

        # 2) function_response must exist
        if not part.function_response:
            raise RuntimeError("Missing function_response on part")

        # 3) .response must exist
        if not part.function_response.response:
            raise RuntimeError("Missing response in function_response")

        function_results.append(part)

        if args.verbose:
            print(f"-> {part.function_response.response}")        

