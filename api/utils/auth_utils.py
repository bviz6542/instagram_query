from fastapi import HTTPException, Header
from api.repositories.auth_repository import get_member_id

def extract_session_token(authorization: str = Header(None)) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid or missing Authorization header")
    return authorization.split(" ")[1]

def get_current_member_id(authorization: str = Header(None)) -> int:
    session_token = extract_session_token(authorization)
    member_id = get_member_id(session_token=session_token)
    if not member_id:
        raise HTTPException(status_code=401, detail="Invalid or expired session token")        
    return member_id