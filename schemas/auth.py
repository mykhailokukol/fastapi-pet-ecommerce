from pydantic import BaseModel

from models.auth import User


# Bases
class UserBase(BaseModel):
    email: str


# CRUD
class UserCreate(UserBase):
    password: str


class UserGet(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
