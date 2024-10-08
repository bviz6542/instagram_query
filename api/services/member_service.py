from sqlalchemy.ext.asyncio import AsyncSession
from api.models.member import MemberModel
from api.schemas.member import MemberCreate
from api.utils.password_utils import hash_password
from api.repositories.member_repository import save

async def create_member(
    member_create: MemberCreate,
    db: AsyncSession
) -> MemberModel:    
    member_create.password = hash_password(member_create.password)
    member = member_create.to_model()
    return await save(member_model=member, db=db)