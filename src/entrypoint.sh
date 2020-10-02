#!/bin/bash

if [[ -z "${1:-}" ]]; then
    echo "Nothin"
else
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser --noinput
    python manage.py runserver $1
fi
