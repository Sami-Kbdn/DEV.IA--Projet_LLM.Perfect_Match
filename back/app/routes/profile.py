from fastapi import APIRouter, Depends
from typing import Annotated
from app.api.db.transaction import get_user

router = APIRouter()

@router.get('/')
async def check_profile(user: Annotated[str, Depends(get_user)]):
    pass

@router.get('/')
async def check_cv(user: Annotated[str, Depends(get_user)]):
    pass

@router.post('/')
async def add_cv(user: Annotated[str, Depends(get_user)]):
    pass

@router.get('/')
async def delete_cv(user: Annotated[str, Depends(get_user)]):
    pass