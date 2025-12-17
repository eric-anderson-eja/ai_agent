from functions.get_file_content import get_file_content
from config import MAX_FILE_CHARS

def run_tests():
    content = get_file_content("calculator", "lorem.txt")
    print("len:", len(content))
    print("endswith trunc msg:", content.endswith(
        f'[...File "lorem.txt" truncated at {MAX_FILE_CHARS} characters]'
    ))

    print('get_file_content("calculator", "main.py"):')
    print(get_file_content("calculator", "main.py"))
    print("-" * 20)

    print('get_file_content("calculator", "pkg/calculator.py"):')
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("-" * 20)

    print('get_file_content("calculator", "/bin/cat"):')
    print(get_file_content("calculator", "/bin/cat"))
    print("-" * 20)

    print('get_file_content("calculator", "pkg/does_not_exist.py"):')
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print("-" * 20)

if __name__ == "__main__":
    run_tests()