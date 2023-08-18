#!/bin/sh
IFS=' ' read -r -a CHANGES < <(echo "$CHANGED_FOLDERS")
for FOLDER in "$CHANGES"
do
  echo "Processing folder: $FOLDER"
done
