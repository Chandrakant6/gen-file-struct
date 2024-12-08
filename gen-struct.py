import os

def parse_structure(file_path):
    """
    Parse the directory structure from a text file.
    
    :param file_path: Path to the text file containing the structure.
    :return: Parsed directory structure as a nested dictionary.
    """
    structure = {}
    current_path = []
    
    with open(file_path, 'r') as file:
        for line in file:
            # Strip leading/trailing whitespace and check for indentation
            stripped_line = line.strip()
            
            # Skip empty lines
            if not stripped_line:
                continue
            
            # Count the number of leading spaces (indicates depth in the tree)
            indent_level = len(line) - len(stripped_line)
            
            # Determine the current directory level based on indentation
            while len(current_path) > indent_level:
                current_path.pop()
            
            # Add the current directory to the path
            current_path.append(stripped_line)
            
            # Add to the structure dictionary
            temp = structure
            for part in current_path:
                temp = temp.setdefault(part, {})
    
    return structure

def create_directories(base_path, structure):
    """
    Recursively create directories based on the given structure.
    
    :param base_path: The base directory where the structure will be created.
    :param structure: The nested dictionary representing the directory tree.
    """
    for dir_name, sub_structure in structure.items():
        full_path = os.path.join(base_path, dir_name)
        
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            print(f"Created directory: {full_path}")
        
        # Recurse to create subdirectories
        create_directories(full_path, sub_structure)

# Main function to read the file and create directories
def main(input_file, base_path='generated_structure'):
    structure = parse_structure(input_file)
    create_directories(base_path, structure)

# Example usage
input_file = 'structure.txt'  # Path to the input text file
main(input_file)
