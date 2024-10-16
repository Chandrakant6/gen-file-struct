#!/bin/bash

create_directory_structure() {
    local content="$1"
    local root_path="$2"
    local current_path="$root_path"
    local prev_indent=0

    echo "$content" | tail -n +2 | while IFS= read -r line; do
        indent=$(echo "$line" | awk '{print length($0) - length(ltrim($0))}')
        dir_name=$(echo "$line" | sed 's/^[[:space:]]*-[[:space:]]*//')

        if [ "$indent" -lt "$prev_indent" ]; then
            cd_count=$((($prev_indent - $indent) / 2))
            for ((i=0; i<cd_count; i++)); do
                current_path=$(dirname "$current_path")
            done
        fi

        mkdir -p "$current_path/$dir_name"
        current_path="$current_path/$dir_name"
        prev_indent=$indent
    done
}

# Check if a file path is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <path_to_structure_file>"
    exit 1
fi

file_path="$1"
root_path=$(basename "$file_path" | sed 's/\.[^.]*$//')

if [ ! -f "$file_path" ]; then
    echo "Error: File not found at $file_path"
    exit 1
fi

content=$(cat "$file_path")

mkdir -p "$root_path"
create_directory_structure "$content" "$root_path"

echo "Directory structure created successfully in '$root_path'!"
