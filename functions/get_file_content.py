from config import MAX_FILE_CHARS
import os
from google import genai
from google.genai import types

schema_get_file_content = {
    "name": "get_file_content",
    "description": "Read the contents of a specific file.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "file_path": {
                "type": "STRING",
                "description": "The path to the file to read."
            }
        },
        "required": ["file_path"]
    }
}


def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        
        if os.path.commonpath([working_dir_abs, target_path]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_path, "r") as f:
            content = f.read(MAX_FILE_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_FILE_CHARS} characters]'
            return content
    
    except Exception as e:
        return f"Error: {e}"
    
        