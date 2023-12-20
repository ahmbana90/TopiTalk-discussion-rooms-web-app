start:
	python manage.py runserver 
install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate 

makemigrations:
	python manage.py makemigrations 

showmigrations:
	python manage.py showmigrations 

sqlmigrate:
	python manage.py sqlmigrate $(app) $(m) 

rollback:
	python manage.py migrate $(app) $(m)

test:
	python manage.py test  
