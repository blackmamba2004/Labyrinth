Запускать контейнеры из /dev

Создайте .env в директории /dev

DB_HOST=test_db
DB_PORT=5432

POSTGRES_DB=your_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password

JWT_SECRET_KEY=your_jwt_secret_key
ALGORITHM=HS256

ACCESS_TOKEN_TTL=0
REFRESH_TOKEN_TTL=0