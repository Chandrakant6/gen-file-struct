import os

def generate_structure(file, root):
    prev_indent = 0
    current_path = ""
    
    with open(file, 'r') as f:
        for line in f:
            indent = len(line) - len(line.lstrip())  # Calculate indent level
            line_content = line.strip().lstrip('-').strip()  # Remove leading spaces and dash
            
            if not line_content:  # Skip empty lines
                continue
            
            # If it's a file (not a directory), create it
            if '.' in line_content:  # Simple check to see if it's a file (e.g., app.py, file.txt)
                # Create the file
                file_path = os.path.join(root, current_path, line_content)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                open(file_path, 'w').close()  # Create an empty file
            else:
                # If it's a directory, adjust the path based on indentation
                if indent > prev_indent:
                    current_path = os.path.join(current_path, line_content)  # Going deeper
                elif indent < prev_indent:
                    current_path = os.path.dirname(current_path)  # Going up
                    current_path = os.path.join(current_path, line_content)
                else:
                    current_path = os.path.join(current_path, line_content)

                # Create the directory
                os.makedirs(os.path.join(root, current_path), exist_ok=True)

            prev_indent = indent  # Update the previous indent level


# Usage
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python generate_structure.py <input_file> <root_directory>")
        sys.exit(1)

    input_file = sys.argv[1]
    root_directory = sys.argv[2]

    generate_structure(input_file, root_directory)
    print("Directory and file structure created successfully.")
