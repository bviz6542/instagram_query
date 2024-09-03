from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.member import MemberCreate
from api.infras.session import get_db
from api.services.member_service import create_member

router = APIRouter()

@router.post("/")
async def register(    
    member_create: MemberCreate,
    db: AsyncSession = Depends(get_db)
):
    await create_member(member_create=member_create, db=db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)