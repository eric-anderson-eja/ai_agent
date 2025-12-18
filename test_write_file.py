# test_write_file.py
import os
from functions.write_file import write_file # Update with your actual folder/file name

# Ensure the test directory exists
if not os.path.exists("calculator"):
    os.makedirs("calculator")

# Test Case 1: Standard file write
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

# Test Case 2: Write with nested directory creation
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

# Test Case 3: Security check (Path traversal attempt)
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))