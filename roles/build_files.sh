#!/bin/bash

echo "BUILD START"

# Install dependencies
python3.12 -m pip install -r requirements.txt

# Collect static files for Django (if using Django)
python3.12 manage.py collectstatic --noinput

echo "BUILD END"

# Clear the screen (optional)
clear
