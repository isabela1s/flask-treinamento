#!/bin/bash

SCRIPT_PATH=$(dirname "$0")

cd "$SCRIPT_PATH"

echo "Subindo os containers..."

docker compose up -d --build

EXIT_CODE=$?

sleep 1

docker ps

exit $EXIT_CODE