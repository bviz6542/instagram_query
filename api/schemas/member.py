from pydantic import BaseModel
from api.models.member import MemberModel

class MemberBase(BaseModel):
    username: str
    password: str

class MemberCreate(MemberBase):
    def to_model(self) -> MemberModel:
        return MemberModel(username=self.username, password=self.password)

class Member(MemberBase):
    id: int

    class Config:
        from_attributes = True