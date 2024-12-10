#!/bin/bash

generate_structure() {
    local file="$1"
    local root="$2"
    local current_path=""
    local prev_indent=0

    while IFS= read -r line; do
        # Calculate the indentation level (leading spaces)
        indent=$(echo "$line" | sed 's/^[[:space:]]*//g' | wc -c)
        # Remove leading spaces and dashes
        name=$(echo "$line" | sed 's/^[[:space:]]*-[[:space:]]*//')

        if [ -z "$name" ]; then continue; fi  # Skip empty lines

        # Check if the name is a file (contains a dot)
        if [[ "$name" == *.* ]]; then
            file_path="$root/$current_path/$name"
            mkdir -p "$(dirname "$file_path")"  # Create parent directories
            touch "$file_path"  # Create the file
        else
            # It's a directory, update the path according to indentation
            if [ "$indent" -gt "$prev_indent" ]; then
                current_path="$current_path/$name"
            elif [ "$indent" -lt "$prev_indent" ]; then
                current_path=$(dirname "$current_path")
                current_path="$current_path/$name"
            else
                current_path="$current_path/$name"
            fi
            mkdir -p "$root/$current_path"  # Create the directory
        fi

        prev_indent=$indent
    done < "$file"
}

# Usage check
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <input_file> <root_directory>"
    exit 1
fi

input_file="$1"
root_dir="$2"

# Ensure the root directory exists
mkdir -p "$root_dir"

# Generate the directory and file structure
generate_structure "$input_file" "$root_dir"
echo "Structure created successfully."
