#!/bin/bash

/app/scripts/wait-for-it.sh db:5432 -t 2 -- 

cd /app/dev

alembic upgrade head

uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload