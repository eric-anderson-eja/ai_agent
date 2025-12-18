from functions.run_python_file import run_python_file 


test_cases = [
    ("calculator", "main.py", None),
    ("calculator", "main.py", ["3 + 5"]),
    ("calculator", "tests.py", None),
    ("calculator", "../main.py", None),
    ("calculator", "nonexistent.py", None),
    ("calculator", "lorem.txt", None),
]

for wd, path, args in test_cases:
    print(f"--- Testing: {path} ---")
    result = run_python_file(wd, path, args)
    print(result)
    print()