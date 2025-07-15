from sqlmodel import SQLModel, Field
from typing import Optional

class CV(SQLModel, table=True):
    cv_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    cv_text: str
    sector : str
