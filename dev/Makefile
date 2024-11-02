build:
	sudo docker compose build

up:
	sudo docker compose up

down:
	sudo docker compose down

build-up:
	sudo docker compose up --build

psql:
	sudo docker exec -it labyrinth_db_dev psql -U dev -d labyrinth_dev

in_app:
	sudo docker exec -it labyrinth_app_dev /bin/bash

in_db:
	sudo docker exec -it labyrinth_db_dev /bin/bash

open_cnt:
	sudo docker exec -it $(container_name) /bin/bash