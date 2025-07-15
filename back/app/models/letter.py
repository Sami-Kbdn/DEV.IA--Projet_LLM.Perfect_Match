# from sqlmodel import SQLModel, Field
# from typing import Optional

# class Letter(SQLModel, table=True):
#     letter_id: Optional[int] = Field(default=None, primary_key=True)
#     job_id: int = Field(foreign_key="job.job_id")
#     user_id: int = Field(foreign_key="user.id")
#     body : str
    