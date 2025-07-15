from sqlmodel import SQLModel, create_engine, Session
from pathlib import Path
import os
from dotenv import load_dotenv
from models.user import User
from models.cv import CV
from models.matching import Matching
# from models.job import Job
# from models.letter import Letter

load_dotenv()

password = os.getenv("PASSWORD")
DATABASE_URL = f"postgresql://postgres:{password}@localhost:5432/Perfect_Match"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def creation():
    SQLModel.metadata.create_all(engine)
