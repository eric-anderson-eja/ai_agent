import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # Will be True or False
        
        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        results = []
        for item in os.listdir(target_dir):
                item_path = os.path.join(target_dir, item)
                
                # Get size and check if it's a dir
                size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                
                results.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(results)
    except Exception as e:
         return f"Error: {str(e)}"
