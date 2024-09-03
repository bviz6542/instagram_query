from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from api.schemas.auth import LoginRequest, LoginResponse
from api.repositories.member_repository import get_by_username
from api.utils.password_utils import verify_password
from api.repositories.auth_repository import get_member_id, save_new_session_token, delete_token
from api.utils.auth_utils import extract_session_token

async def create_auth(
    login_request: LoginRequest, 
    db: AsyncSession
) -> LoginResponse:
    member = await get_by_username(username=login_request.username, db=db)
    if verify_password(login_request.password, member.password):
        access_token = save_new_session_token(member.id)
        return LoginResponse(access_token=access_token)
    else:
        raise HTTPException(status_code=401, detail="Password is not correct")
    
async def delete_auth(
    authorization: str
):
    session_token = extract_session_token(authorization)
    member_id = get_member_id(session_token=session_token)
    if not member_id:
        raise HTTPException(status_code=403, detail="Invalid or expired session token")        
    delete_token(session_token=session_token)