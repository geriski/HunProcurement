web: python manage.py runserver
web: gunicorn hun_proc/hun_proc.wsgi --log-file -
heroku ps:scale web=1