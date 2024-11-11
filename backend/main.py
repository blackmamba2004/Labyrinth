from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.pkg.auth.transport.router import router as auth_router
from backend.internal.users.router import router as users_router
from backend.internal.levels.router import router as levels_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # разрешаем доступ с любого источника
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(levels_router)
