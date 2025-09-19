#!/bin/bash

# Exit immediately on error
set -e

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi

# Activate venv
source .venv/bin/activate

# Upgrade pip
#pip install --upgrade pip

# Install dependencies
#pip install -r requirements.txt


python3 main.py


