
DOCKER_COMPOSE_FILE="docker/dev.docker-compose.test.yml"


if [ ! -f "$DOCKER_COMPOSE_FILE" ]; then
    echo "Error: File $DOCKER_COMPOSE_FILE not found in $PROJECT_DIR"
    exit 1
fi

docker-compose -f "$DOCKER_COMPOSE_FILE" down -v
docker-compose -f "$DOCKER_COMPOSE_FILE" up --build -d

echo "Waiting for database to be ready..."
DB_CONTAINER=$(docker ps -qf "name=docker-test_db")
if [ -z "$DB_CONTAINER" ]; then
    echo "Error: Database container 'docker-test_db' not found"
    docker-compose -f "$DOCKER_COMPOSE_FILE" down -v
    exit 1
fi


while ! docker exec "$DB_CONTAINER" pg_isready -U postgres > /dev/null 2>&1; do
  sleep 1
done

WEB_CONTAINER=$(docker ps -qf "name=docker-test_web")
if [ -z "$WEB_CONTAINER" ]; then
    echo "Error: Web container 'docker-test_web' not found"
    docker-compose -f "$DOCKER_COMPOSE_FILE" down -v
    exit 1
fi

STATUS=$(docker inspect --format '{{.State.Status}}' "$WEB_CONTAINER")
if [ "$STATUS" != "running" ]; then
    echo "Error: Web container is not running (status: $STATUS)"
    docker-compose -f "$DOCKER_COMPOSE_FILE" down -v
    exit 1
fi

echo "Running tests..."
docker exec "$WEB_CONTAINER" python manage.py test apps --settings=api.settings

echo "Cleaning up..."
docker-compose -f "$DOCKER_COMPOSE_FILE" down -v
