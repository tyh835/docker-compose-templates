# Docker Compose Templates

Sample deployment configurations using Docker Compose

## nginx-uwsgi-flask-redis

Full-stack setup of Nginx + uWSGI + Flask + Redis using Docker Compose. Start the service by running: `docker-compose up -d`

Nginx can also load-balance multiple Flask containers. Start multiple Flask containers by running:

`docker-compose up -d --scale web=NUMBER_OF_CONTAINERS`

Note that by default, Nginx runs on `http://localhost:8080`, but this can be changed by configuring `docker-compose.yml`.