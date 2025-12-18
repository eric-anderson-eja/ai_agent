import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        
        if os.path.commonpath([working_dir_abs, target_path]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
                return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith(".py"):
             return f'Error: "{file_path}" is not a Python file'
        
        # build command
        command = ["python", target_path]
        if args:
             command.extend(args)

        # execute subprocess
        result = subprocess.run(
             command, 
             cwd=working_dir_abs,
             capture_output=True,
             text=True,
             timeout=30
        )

        output_parts = []
                
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        
        if result.stdout:
            output_parts.append(f"STDOUT: {result.stdout}")
        
        if result.stderr:
            output_parts.append(f"STDERR: {result.stderr}")
            
        if not result.stdout and not result.stderr:
            output_parts.append("No output produced")

        return "\n".join(output_parts).strip()

    except subprocess.TimeoutExpired:
        return "Error: executing Python file: Process timed out after 30 seconds"
    except Exception as e:
        return f"Error: executing Python file: {e}"

