build:
	docker compose build

up:
	docker compose up

down:
	docker compose down

down-no-data:
	docker compose down -v

build-up:
	docker compose up --build

psql:
	docker exec -it labyrinth_db_dev psql -U dev -d dev_db

in_app:
	docker exec -it labyrinth_app_dev /bin/bash

in_db:
	docker exec -it labyrinth_db_dev /bin/bash