from fastapi import APIRouter
from api.endpoints import member

# TODO: add friendship
api_router = APIRouter()
api_router.include_router(member.router, prefix="/members", tags=["member"])