# Newspaper agency service

Newspaper agency service is a Django-based application for newspaper management.

### Getting Started

```
git clone git@github.com:oleksashcherbakov/newspaper-agency.git
cd newspaper-agency
python - m venv venv
sourse venv/bin/activate
pip install - r requiments.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
```

#### Architecture diagram
![DB schema](static/photo_2024-10-27_14-24-29.jpg)


### Admin Interface
The Django admin interface is available at /admin/. You can use it to manage the database entries directly.

### Debug Toolbar
The Django Debug Toolbar is included in the project. It's automatically added to the URL patterns when in debug mode.
