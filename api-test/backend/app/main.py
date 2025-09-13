from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database.database import db
from .database.user_repository import UserModel
from .routers import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    if db.is_closed():
        db.connect()
    db.create_tables([UserModel])

    print("Database connected and tables created")

    yield

    if not db.is_closed():
        db.close()
    print("Database connection closed")


app = FastAPI(lifespan=lifespan)
app.include_router(users.router)


@app.get("/")
def root():
    return "Hello, Root!"
