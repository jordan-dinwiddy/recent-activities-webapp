recent-activities-webapp
========================

My first Django webapp

Setup
-----
1. You'll need Django installed first. You can test with `python -c "import django; print(django.get_version())"`.
2. Update mysite/settings.py with your preferred database. If using sqlite3 then just update the config to point to good location for your db file.
3. Create the database schemas with `python manage.py syncdb`

How to run
----------
    python manage.py runserver

And then browse to http://127.0.0.1:8000/activities

Running unit tests
------------------
    python manage.py test  
