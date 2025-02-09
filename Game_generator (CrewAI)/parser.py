import os
import re

def parse(file_path):
    """
    Parses the specified markdown file to extract file paths and corresponding code blocks.
    Then writes each code block to its designated file, ensuring that all files are created
    relative to the current working directory.

    Expected file format in code.md:

        Path: relative/path/to/file.py
        Code:
        '''
        # Complete executable game code or other file content here.
        '''

    Multiple file blocks can be included in the markdown.
    """
    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        return

    with open(file_path, 'r') as f:
        content = f.read()

    # Regular expression to capture each file block.
    pattern = r"Path:\s*(?P<filepath>.+?)\s*Code:\s*'''(?P<code>.*?)'''"
    matches = re.finditer(pattern, content, re.DOTALL)

    files_created = 0

    for match in matches:
        filepath = match.group("filepath").strip()
        code = match.group("code").strip()

        # Ensure the filepath is relative: if it starts with '/', remove it.
        if filepath.startswith('/'):
            filepath = filepath.lstrip('/')

        # Create the full path relative to the current working directory.
        full_path = os.path.join(os.getcwd(), filepath)

        # Create directory if it doesn't exist.
        directory = os.path.dirname(full_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            print(f"Created directory: {directory}")

        # Write the extracted code to the target file.
        with open(full_path, 'w') as f:
            f.write(code)
        print(f"Wrote code to '{full_path}'")
        files_created += 1

    if files_created == 0:
        print("No valid file blocks found in the output.")
    else:
        print(f"Successfully created {files_created} file(s).")
