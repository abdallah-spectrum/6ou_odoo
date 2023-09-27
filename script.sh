#!/bin/bash

# Check if re_list.txt exists
if [ -e "applist.txt" ]; then
    # Read the list of folder names from re_list.txt into an array
    mapfile -t folders_to_remove < applist.txt

    # Loop through the array and remove matching folders
    for folder in "${folders_to_remove[@]}"; do
        if [ -d "$folder" ]; then
            echo "Removing folder: $folder"
            rm -r "$folder"
        else
            echo "Folder not found: $folder"
        fi
    done
else
    echo "re_list.txt not found in the current directory."
fi

