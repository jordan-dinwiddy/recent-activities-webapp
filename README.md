recent-activities-webapp
========================

My first Django webapp

Setup
-----
1. Updating mysite/settings.py with your preferred database. If using sqlite3 then just update the config to point to good location for your db file.
2. Create the database schemas:

    python manage.py syncdb

How to run
----------
    python manage.py runserver
    
And then browse to http://127.0.0.1:8000/activities

