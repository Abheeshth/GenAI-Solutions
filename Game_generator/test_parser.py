import os
from parser import parse_code_output

def main():
    # Specify the path to the code.md file (assumed to be in the current directory)
    code_md_path = os.path.join(os.getcwd(), "code.md")
    
    if not os.path.exists(code_md_path):
        print(f"File not found: {code_md_path}")
        return

    print(f"Processing file: {code_md_path}\n")
    # Call the parser function to process the file
    parse_code_output(code_md_path)

if __name__ == "__main__":
    main()
