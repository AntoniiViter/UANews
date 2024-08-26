#!/bin/bash

# Check if the virtual environment directory exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found! Please create one first."
    exit 1
fi

# Activate the virtual environment
source venv/bin/activate

# Navigate to the Django project directory (relative path)
cd "$(dirname "$0")"

# Run the Django development server
python manage.py runserver

# Deactivate virtual environment after stopping the server
deactivate