from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from models.cv import CV
from schemas.load_cv import CVRead
from utils.jwt_handler import get_user
from db.session import get_session
from typing import Annotated

router = APIRouter()

@router.get("/", response_model=List[CVRead])
async def get_user_cvs(
    user: Annotated[str, Depends(get_user)],
    session: Session = Depends(get_session)
):
    cvs = session.exec(select(CV).where(CV.user_id == user.id)).all()
    return cvs
