run:
	docker build
	# docker-compose is the old way (as in the course) - you should use docker compose (without -)
	# docker-compose build # old way
	# docker-compose up # old way
	# docker-compose run app django-admin.py startproject app . # old way
	# docker-compose run app python manage.py startapp core # oldway

	docker compose build --no-cache
	docker compose up
	docker compose run app django-admin.py startproject app .
	docker compose run app python manage.py startapp core

	# FIXME running with basic python server is for developing only. Should I use unicorn or any other python wsgi/web server
	docker exec $(docker container ls -q) python manage.py runserver 0.0.0.0:8000

	# running wirh docker-compose run app python manage.py runserver 0.0.0.0:8000 won't work 'cause it don't start bind to any port. You should run it with docker-compose up after docker exec
