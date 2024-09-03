from fastapi import APIRouter
from api.endpoints import member, auth

# TODO: add friendship
api_router = APIRouter()
api_router.include_router(member.router, prefix="/members", tags=["member"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])