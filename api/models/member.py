from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from api.infras.postgresql import Base

class MemberModel(Base):
    __tablename__ = "member"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)