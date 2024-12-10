import os

def generate_structure(file, root):
    prev_indent = 0
    current_path = ""

    with open(file, 'r') as f:
        for line in f:
            # Calculate the number of leading spaces to determine indentation
            indent = len(line) - len(line.lstrip())
            # Get the directory name by stripping leading spaces and '-'
            dir_name = line.strip().lstrip('-').strip()

            # Adjust the path based on indentation
            if indent > prev_indent:
                current_path = os.path.join(current_path, dir_name)
            elif indent < prev_indent:
                # Go up in the directory tree
                current_path = os.path.dirname(current_path)
                current_path = os.path.join(current_path, dir_name)
            else:
                # Same level as before
                current_path = os.path.join(current_path, dir_name)

            # Create the directory
            os.makedirs(os.path.join(root, current_path), exist_ok=True)

            # Update previous indent level
            prev_indent = indent


# Usage check
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python generate_structure.py <input_file> <root_directory>")
        sys.exit(1)

    input_file = sys.argv[1]
    root_directory = sys.argv[2]

    # Generate the directory structure
    generate_structure(input_file, root_directory)
    print("Directory structure created successfully.")
