from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from api.models.member import MemberModel
from fastapi import HTTPException

def save(member_model: MemberModel, db: Session) -> MemberModel:
    db.add(member_model)
    try:
        db.commit()
        db.refresh(member_model)
        return member_model
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Username already exists.")