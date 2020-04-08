#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
# Collect static files
echo "Collect static files"
python manage.py collectstatic --no-input --clear

# Apply database migrations
echo "Apply database migrations"
python manage.py init_pyerp

# Install plugins in testing
echo "Install plugins in testing"
python manage.py init_purchase
python manage.py init_sale
python manage.py init_account

# Start server
echo "Starting server"
bin/gunicorn_start.sh

exec "$@"