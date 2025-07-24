from sqlmodel import Session
from app.db.session import get_session
from app.utils.jwt_handler import get_user
from typing import Annotated
from fastapi import APIRouter, Depends
from app.schemas.load_cv import CVCreate, CVRead
from app.models.cv import CV

router = APIRouter()

@router.post("/", response_model=CVRead)
async def load_cv(
    data: CVCreate,
    user: Annotated[str, Depends(get_user)],
    session: Session = Depends(get_session)
):
    cv = CV(
        cv_text=data.cv_text,
        sector=data.sector,
        user_id=user.id
    )

    session.add(cv)
    session.commit()
    session.refresh(cv)
    return cv