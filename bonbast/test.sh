#!/bin/sh
mapfile -t CHANGES < <(echo $CHANGED_FOLDERS)
for FOLDER in "$CHANGES"
do
  echo "Processing folder: $FOLDER"
done
