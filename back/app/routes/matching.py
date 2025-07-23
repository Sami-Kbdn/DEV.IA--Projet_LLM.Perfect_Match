from sqlmodel import Session, select
from db.session import get_session
from utils.jwt_handler import get_user
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from schemas.matching import MatchingRequest, MatchingResponse
from models.matching import Matching
from models.cv import CV
from llm import generate_matching

router = APIRouter()

from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlmodel import Session, select
from llm import generate_matching  

router = APIRouter()

@router.post("/", response_model=MatchingResponse)
async def create_matching(
    data: MatchingRequest,
    user: Annotated[str, Depends(get_user)],
    # user: Annotated[User, Depends(get_user)]
    session: Session = Depends(get_session)
):
    # Vérifie que le CV existe et appartient à l'utilisateur
    load_cv = session.exec(
        select(CV).where((CV.cv_id == data.cv_id) & (CV.user_id == user.id))
    ).first()

    if not load_cv:
        raise HTTPException(status_code=404, detail="CV introuvable ou ne vous appartient pas")

    if not data.job_description:
        raise HTTPException(status_code=400, detail="La description du job est vide")

    llm_result = generate_matching(load_cv.cv_text, data.job_description)

    score = llm_result["score"]
    feedback = llm_result["feedback"]

    new_matching = Matching(
        user_id=user.id,
        cv_id=data.cv_id,
        score=score,
        feedback=feedback
    )

    session.add(new_matching)
    session.commit()
    session.refresh(new_matching)

    return {"score": score, "feedback": feedback}
