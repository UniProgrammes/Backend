migrate:
	docker compose -f docker/dev.docker-compose.yml up -d
	docker compose -f docker/dev.docker-compose.yml exec web python3 manage.py migrate
	docker compose -f docker/dev.docker-compose.yml down

makemigrations:
	docker compose -f docker/dev.docker-compose.yml up -d
	docker compose -f docker/dev.docker-compose.yml exec web python3 manage.py makemigrations
	docker compose -f docker/dev.docker-compose.yml down

runserver:
	docker compose -f docker/dev.docker-compose.yml up

shell:
	docker compose -f docker/dev.docker-compose.yml up -d
	docker compose -f docker/dev.docker-compose.yml exec web python3 manage.py shell
	docker compose -f docker/dev.docker-compose.yml down

build:
	docker compose -f docker/dev.docker-compose.yml build

up:
	docker compose -f docker/dev.docker-compose.yml up -d

down:
	docker compose -f docker/dev.docker-compose.yml down

initdb:
	docker compose -f docker/dev.docker-compose.yml up -d
	docker compose -f docker/dev.docker-compose.yml exec web python3 manage.py initdb
	docker compose -f docker/dev.docker-compose.yml down

createsuperuser:
	docker compose -f docker/dev.docker-compose.yml up -d
	docker compose -f docker/dev.docker-compose.yml exec web python3 manage.py createsuperuser
	docker compose -f docker/dev.docker-compose.yml down

show_urls:
	docker compose -f docker/dev.docker-compose.yml up -d
	docker compose -f docker/dev.docker-compose.yml exec web python3 manage.py show_urls
	docker compose -f docker/dev.docker-compose.yml down

# PRODUCTION commands
migrate-prod:
	docker compose -f docker/docker-compose.yml up -d
	docker compose -f docker/docker-compose.yml exec web python3 manage.py migrate
	docker compose -f docker/docker-compose.yml down

runserver-prod:
	docker compose -f docker/docker-compose.yml up

build-prod:
	docker compose -f docker/docker-compose.yml build

up-prod:
	docker compose -f docker/docker-compose.yml up -d

down-prod:
	docker compose -f docker/docker-compose.yml down
