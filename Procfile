release: python manage.py migrate && python manage.py fetchlanguages && python manage.py fetchtopten
web: cd stargazer && gunicorn stargazer.wsgi --log-file -
