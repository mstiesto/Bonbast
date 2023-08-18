#!/bin/sh
IFS=',' read -ra CHANGES <<< "$CHANGED_FOLDERS"
for FOLDER in "$CHANGES"
do
  echo "Processing folder: $FOLDER"
done
