import pandas as pd

# Load the Excel file
file_path = ''  # Replace with your actual file path
df = pd.read_excel(file_path)

# Convert each row to a list
chunks = df.values.tolist()

# File to save the output
output_file_path = 'output.txt'

# Write each chunk to the text file with separator
with open(output_file_path, 'w') as file:
    for chunk in chunks:
        # Convert list to string and add separator
        file.write(str(chunk) + "\n\n")

print(f"Data written to {output_file_path}")

