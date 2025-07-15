from fastapi import FastAPI
from contextlib import asynccontextmanager
# from app.api.v1.endpoints import auth, users
from db.session import engine, creation
from sqlmodel import SQLModel
from routes import letter, auth, matching, load_cv

app = FastAPI(title="fastapi")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(matching.router, prefix="/matching", tags=["matching"])
app.include_router(load_cv.router, prefix="/load_cv", tags=["load_cv"])
# app.include_router(letter.router, prefix="/letter", tags=["letter"])


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

creation()