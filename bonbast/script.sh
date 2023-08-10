#!/bin/bash
ls -ltr
buildah login -u "$DOCKER_USER" -p "$DOCKER_TOKEN" docker.io
# Create an empty array
array=()
# Use a while loop to read each line of the string
while IFS= read -r line; do
array+=("$line")  # Append each line to the array
done <<< "$CHANGED_FOLDERS"

for folder in "${array[@]}"; do
  echo "Processing folder: $folder"

  FOLDER_PATH=./$folder
  IMAGE_URL=$(params.IMAGE)/$folder:$(params.DOCKER_TAG)

  buildah --storage-driver=$(params.STORAGE_DRIVER) bud -f $FOLDER_PATH/Dockerfile -t $IMAGE_URL $FOLDER_PATH && \
  buildah --storage-driver=$(params.STORAGE_DRIVER) push $IMAGE_URL
done
