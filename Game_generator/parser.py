import os
import re

def parse_code_output(file_path):
    """
    Parses a markdown file (code.md) that contains multiple file blocks.
    Each block starts with a "Path:" line, followed by one or more triple-quoted sections.
    All triple-quoted sections within the block are concatenated (with a newline) to form the final content.
    
    The function then:
      - Creates a directory if the path is a directory (ends with "/" or has no file extension).
      - Otherwise, creates parent directories as needed and writes the concatenated content to the file.
    
    Example block formats in code.md:
    
        Path: some_folder/
        '''
        # This is a comment for the folder.
        '''
    
        Path: some_folder/main.py
        '''
        # A brief description.
        '''
        Code:
        '''
        import pygame
        # More code...
        '''
    
    All triple-quoted sections for a given path will be merged.
    """
    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        return

    # Read the entire file
    with open(file_path, 'r', encoding="utf-8") as f:
        content = f.read()

    # Split the file into blocks using "Path:" as the delimiter.
    # The lookahead (?=Path:) ensures we keep the "Path:" in each block.
    blocks = re.split(r'(?=Path:\s*)', content)
    items_created = 0

    for block in blocks:
        block = block.strip()
        if not block.startswith("Path:"):
            continue  # skip any block that doesn't start with "Path:"
        
        # Extract the file path from the first line.
        lines = block.splitlines()
        if not lines:
            continue

        # Remove "Path:" prefix and extract the path.
        raw_path = lines[0][len("Path:"):].strip()
        # Remove any accidental extra content after the path (e.g. stray markers)
        file_path_str = raw_path.split()[0].strip()

        # Combine all triple-quoted blocks in this segment.
        # This pattern matches ''' ... '''
        code_blocks = re.findall(r"'''(.*?)'''", block, re.DOTALL)
        # Clean and join all found blocks.
        final_content = "\n".join([c.strip() for c in code_blocks if c.strip()])

        # Build the full path relative to current working directory.
        full_path = os.path.join(os.getcwd(), file_path_str)

        # Determine if this block represents a directory.
        # We consider it a directory if it ends with a slash or if the basename has no extension.
        is_directory = file_path_str.endswith("/") or os.path.splitext(os.path.basename(file_path_str))[1] == ''

        if is_directory:
            # Create the directory if it doesn't exist.
            try:
                os.makedirs(full_path, exist_ok=True)
                print(f"Created directory: {full_path}")
                items_created += 1
            except Exception as e:
                print(f"Failed to create directory '{full_path}': {e}")
            continue  # No file writing for directories

        # For file blocks, ensure the parent directory exists.
        parent_dir = os.path.dirname(full_path)
        if parent_dir and not os.path.exists(parent_dir):
            try:
                os.makedirs(parent_dir, exist_ok=True)
                print(f"Created directory: {parent_dir}")
            except Exception as e:
                print(f"Failed to create directory '{parent_dir}': {e}")

        # Write the final content to the file.
        try:
            with open(full_path, 'w', encoding="utf-8") as f:
                f.write(final_content)
            print(f"Wrote content to '{full_path}'")
            items_created += 1
        except Exception as e:
            print(f"Failed to write to '{full_path}': {e}")

    if items_created == 0:
        print("No valid file or directory blocks found in the output.")
    else:
        print(f"Successfully created {items_created} item(s).")
