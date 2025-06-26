web: gunicorn --bind 0.0.0.0:$PORT Maor_proj.mysite.wsgi:application
release: python manage.py migrate && python manage.py collectstatic --noinput
