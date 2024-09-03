from api.infras.redis import get_value, set_value, delete_key
from uuid import uuid4
from typing import Optional
from fastapi import HTTPException

def get_member_id(session_token: str) -> Optional[int]:
    member_id = get_value(session_token)
    if not member_id:
        raise HTTPException(status_code=404, detail="Session expired or invalid")
    try:
        return int(member_id)
    except ValueError:
        return HTTPException(status_code=404, detail="Invalid session info")

def save_new_session_token(id: str) -> str:
    session_token = str(uuid4())
    set_value(session_token, id, expiration_time=3600)
    return session_token

def delete_token(session_token: str):
    delete_key(session_token)