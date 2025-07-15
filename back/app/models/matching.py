from sqlmodel import SQLModel, Field
from typing import Optional

class Matching(SQLModel, table=True):
    matching_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    cv_id: int = Field(foreign_key="cv.cv_id")
    score : int
    feedback : str