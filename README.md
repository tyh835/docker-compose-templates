# Docker Compose Templates

Sample deployment configurations using Docker Compose

## flask-redis-postgres

docker-compose verision: 1.23.2

Optimized Flask image connected to Redis and PostgreSQL. Test out the application with `docker-compose up`.

By default, the application runs at `localhost:8000`.

## nginx-uwsgi-flask-redis

docker-compose version: 1.23.2

Full-stack setup of Nginx + uWSGI + Flask + Redis using Docker Compose. Start the service by running: `docker-compose up`

Nginx can also load-balance multiple Flask containers. Start multiple Flask containers by running:

`docker-compose up ---scale web=NUMBER_OF_CONTAINERS`

Note that by default, Nginx runs on `http://localhost:8080`, but this can be changed by configuring `docker-compose.yml`.
