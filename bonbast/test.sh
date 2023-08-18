#!/bin/sh
mapfile -t CHANGES < <$CHANGED_FOLDERS
IFS=' ' read -r CHANGES < <(echo "$CHANGED_FOLDERS")
for FOLDER in "$CHANGES"
do
  echo "Processing folder: $FOLDER"
done
