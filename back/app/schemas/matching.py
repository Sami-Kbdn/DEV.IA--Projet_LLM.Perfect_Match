from pydantic import BaseModel

class MatchingRequest(BaseModel):
    cv_id: int
    job_description: str

class MatchingResponse(BaseModel):
    score: int
    feedback: str
