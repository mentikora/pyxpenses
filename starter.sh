#!/usr/bin/env bash

PROJECT_NAME="${1#--name=}"

mkdir "$PROJECT_NAME"

cp .gitignore-base "$PROJECT_NAME/.gitignore"

cd "$PROJECT_NAME"
uv init