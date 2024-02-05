Install:

poetry update package

poetry shell

docker pull postgres

docker run --name hw10-app-postgres -p 5432:5432 -e POSTGRES_PASSWORD=8032573 -d postgres

python manage.py migrate

python manage.py createsuperuser

python manage.py loadauthors data/authors.json

python manage.py loadquotes data/quotes.json

python manage.py runserver