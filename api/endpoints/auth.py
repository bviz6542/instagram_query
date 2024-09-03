from fastapi import APIRouter, Depends, Header, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.auth_service import create_auth, delete_auth
from api.infras.postgresql import get_db
from api.schemas.auth import LoginRequest, LoginResponse

router = APIRouter()

@router.post("/login/")
async def login(
    login_request: LoginRequest,
    db: AsyncSession = Depends(get_db)
) -> LoginResponse:
    login_response = await create_auth(login_request=login_request, db=db)
    return login_response

@router.delete("/logout/")
async def logout(
    authorization: str = Header(None)
):
    await delete_auth(authorization=authorization)
    return Response(status_code=status.HTTP_204_NO_CONTENT)