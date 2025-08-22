#!/usr/bin/env bash

PROJECT_NAME="${1#--name=}"

if [ -z "$PROJECT_NAME" ] || [ "$PROJECT_NAME" = "$1" ]; then
  echo "Usage: $0 --name=project-name"
  exit 1
fi

if [ -d "$PROJECT_NAME" ]; then
  echo "[Failed]: Folder exists"
else
  echo "Creating folder..."
  mkdir "$PROJECT_NAME"

  echo "Copying gitignore..."
  cp .gitignore-base "$PROJECT_NAME/.gitignore"

  cd "$PROJECT_NAME"

  uv init
fi
