from sqlalchemy.orm import Session

from models import auth


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(auth.User).offset(skip).limit(limit).all()
