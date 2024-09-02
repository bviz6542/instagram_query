from fastapi import APIRouter
from endpoints import member

api_router = APIRouter()
api_router.include_router(member.router, prefix="/members", tags=["member"])