from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.database import get_db
from controllers.auth import get_users
from schemas import auth


auth_router = APIRouter()


@auth_router.get("/users", response_model=list[auth.UserGet])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(skip=skip, limit=limit, db=db)
    return users
