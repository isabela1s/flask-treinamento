#!/bin/bash

SCRIPT_PATH=$(dirname "$0")

cd "$SCRIPT_PATH"

sh down.sh && sh up.sh