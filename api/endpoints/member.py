from fastapi import APIRouter, Depends, Response, status, Query
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/")
async def get_member() -> str:
    return "good"