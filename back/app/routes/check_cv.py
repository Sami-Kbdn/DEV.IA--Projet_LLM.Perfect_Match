from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List, Annotated
from app.models.cv import CV
from app.schemas.load_cv import CVRead
from app.utils.jwt_handler import get_user
from app.db.session import get_session

router = APIRouter()

@router.get("/", response_model=List[CVRead])
async def get_user_cvs(
    user: Annotated[str, Depends(get_user)],
    session: Session = Depends(get_session)
):
    cvs = session.exec(select(CV).where(CV.user_id == user.id)).all()
    return cvs
