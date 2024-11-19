#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $DB_HOST $DB_PORT; do
        sleep 0.1
    done
    echo "PostgreSQL started"
fi

# Run migrations
python manage.py makemigrations --no-input
python manage.py migrate

# Execute the main command
exec "$@"