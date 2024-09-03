from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError
from api.models.member import MemberModel
from fastapi import HTTPException

async def save(
    member_model: MemberModel, 
    db: AsyncSession
) -> MemberModel:
    db.add(member_model)
    try:
        await db.commit()
        await db.refresh(member_model)
        return member_model
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=409, detail="Username already exists.")