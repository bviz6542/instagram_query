from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
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

async def get_by_username(
    username: str,
    db: AsyncSession
) -> MemberModel:
    query = select(MemberModel).filter_by(username=username)
    result = await db.execute(query)
    member = result.scalars().first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not registered")
    return member