from pydantic import BaseModel

class CVCreate(BaseModel):
    cv_text: str
    sector: str

class CVRead(BaseModel):
    cv_id: int
    cv_text: str
    user_id: int

    class Config:
        orm_mode = True


