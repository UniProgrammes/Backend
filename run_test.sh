#!/bin/bash

# Percorso assoluto della directory del progetto
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Nome del file Docker Compose
DOCKER_COMPOSE_FILE="docker/dev.docker-compose.test.yml"

# Verifica che il file Docker Compose esista
if [ ! -f "$PROJECT_DIR/$DOCKER_COMPOSE_FILE" ]; then
    echo "Error: File $DOCKER_COMPOSE_FILE not found in $PROJECT_DIR"
    exit 1
fi

# Avvia i container Docker per i test
docker-compose -f "$PROJECT_DIR/$DOCKER_COMPOSE_FILE" up --build -d

# Attendi che il database sia pronto
echo "Waiting for database to be ready..."
DB_CONTAINER=$(docker ps -qf "name=docker-test_db")
if [ -z "$DB_CONTAINER" ]; then
    echo "Error: Database container 'docker-test_db' not found"
    docker-compose -f "$PROJECT_DIR/$DOCKER_COMPOSE_FILE" down -v
    exit 1
fi

while ! docker exec "$DB_CONTAINER" pg_isready -U postgres > /dev/null 2>&1; do
  sleep 1
done

# Trova il container del servizio web
WEB_CONTAINER=$(docker ps -qf "name=docker-web")
if [ -z "$WEB_CONTAINER" ]; then
    echo "Error: Web container 'docker-web' not found"
    docker-compose -f "$PROJECT_DIR/$DOCKER_COMPOSE_FILE" down -v
    exit 1
fi

# Verifica lo stato del container web
STATUS=$(docker inspect --format '{{.State.Status}}' "$WEB_CONTAINER")
if [ "$STATUS" != "running" ]; then
    echo "Error: Web container is not running (status: $STATUS)"
    docker-compose -f "$PROJECT_DIR/$DOCKER_COMPOSE_FILE" down -v
    exit 1
fi

# Esegui i test
echo "Running tests..."
docker exec "$WEB_CONTAINER" python manage.py test apps --settings=api.test_settings

# Arresta e rimuovi i container
echo "Cleaning up..."
docker-compose -f "$PROJECT_DIR/$DOCKER_COMPOSE_FILE" down -v
