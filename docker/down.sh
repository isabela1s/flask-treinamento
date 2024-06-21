#!/bin/bash

SCRIPT_PATH=$(dirname "$0")

cd "$SCRIPT_PATH"

echo "Descendo os containers..."

docker compose down