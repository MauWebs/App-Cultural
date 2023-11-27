#!/usr/bin/env bash
# exit on error
set -o errexit

# Packages
pip install -r requirements.txt

# Data Base
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate