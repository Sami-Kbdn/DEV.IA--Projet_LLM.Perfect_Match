# A RAJOUTER POUR PROJET FIL ROUGE : A RELIER AVEC JOB




# from fastapi import APIRouter, Depends, HTTPException, status
# from typing import Annotated
# from utils.jwt_handler import get_user
# from schemas.letter import LetterCreate,LetterOut
# from sqlmodel import Session, select
# from db.session import get_session
# from models.job import Job
# from models.cv import CV
# from models.letter import Letter

# router = APIRouter()

# @router.post("/", response_model=LetterOut)
# async def create_letter(
#     data: LetterCreate,
#     user: Annotated[str, Depends(get_user)],
#     session: Session = Depends(get_session)
# ):
#     job_stmt = select(Job).where(Job.job_id == data.job_id, Job.user_id == user.id)
#     db_job = session.exec(job_stmt).first()

#     cv_stmt = select(CV).where(CV.cv_id == data.cv_id, CV.user_id == user.id)
#     db_cv = session.exec(cv_stmt).first()

#     if not db_job or not db_cv:
#         raise HTTPException(
#             status_code=404,
#             detail="Le CV ou l'offre d'emploi n'existent pas ou ne vous appartiennent pas."
#         )
 
#     fake_letter = ("fake text")
#     letter = Letter(
#         job_id=db_job.job_id,
#         user_id=user.id,
#         body=fake_letter
#     )

#     session.add(letter)
#     session.commit()
#     session.refresh(letter)

