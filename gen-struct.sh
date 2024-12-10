#!/bin/bash

gen_struct() {
    local file="$1"
    local root="$2"
    local current_path=""

    while IFS= read -r line; do
        indent=$(echo "$line" | awk '{print length($0) - length(ltrim($0))}')
        dir_name=$(echo "$line" | sed 's/^[[:space:]]*-[[:space:]]*//')

        # Adjust path based on indentation
        if [ "$indent" -gt "$prev_indent" ]; then
            current_path="$current_path/$dir_name"
        elif [ "$indent" -lt "$prev_indent" ]; then
            current_path=$(dirname "$current_path")
            current_path="$current_path/$dir_name"
        else
            current_path="$current_path/$dir_name"
        fi

        mkdir -p "$root/$current_path"
        prev_indent=$indent
    done < "$file"
}

# Usage
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <input_file> <root_directory>"
    exit 1
fi

gen_struct "$1" "$2"
