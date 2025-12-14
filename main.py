import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types



# ***** Configuration *****
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
args = parser.parse_args()
user_prompt = args.user_prompt
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

# ****  Core Logic  ***
response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents=messages
    )

#  ***** Validation and Output *****
if response.usage_metadata == 'None':
    raise RuntimeError("POSSIBLE FAILED REQUEST, no token metadata")

print(f"User prompt: {user_prompt}")
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(f"Response:\n{response.text}")

