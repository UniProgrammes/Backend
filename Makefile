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


