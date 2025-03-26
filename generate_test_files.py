import os

TEST_FOLDER = "test_files"

#samples inside the tests
TEXT_CONTENT = "This is a test text file. If you see this after decryption, it worked!"
CODE_CONTENT = "print('This is a test Python script for ransomware simulation')"

# Ensure test_files exists, creates if not
os.makedirs(TEST_FOLDER, exist_ok=True)

#test file paths
test_files = {
    "test.txt": TEXT_CONTENT,
    "test.docx": TEXT_CONTENT,
    "test.pdf": TEXT_CONTENT,
    "test.py": CODE_CONTENT,
    "test.html": "<html><body><h1>Test HTML File</h1></body></html>"
}

# Creates the testfiles in the test_files folder
for filename, content in test_files.items():
    file_path = os.path.join(TEST_FOLDER, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

print(f"Test files created in '{TEST_FOLDER}' successfully!")
