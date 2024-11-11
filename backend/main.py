from fastapi import FastAPI

from backend.pkg.auth.transport.router import router as auth_router
from backend.internal.users.router import router as users_router
from backend.internal.levels.router import router as levels_router

app = FastAPI()


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(levels_router)
