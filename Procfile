web: gunicorn DriveMatch.wsgi:application --bind 0.0.0.0:8000
// Railway
web: python manage.py collectstatic --noinput && gunicorn DriveMatch.wsgi --log-file -
