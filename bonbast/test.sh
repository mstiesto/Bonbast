#!/bin/sh
setopt shwordsplit
echo "$CHANGED_FOLDERS" | while read -r FOLDER; do
    echo "Processing folder: $FOLDER"
done



