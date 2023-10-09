from fastapi import FastAPI

from models.database import engine
from models import auth

from routers.auth import auth_router


auth.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=auth_router, prefix="/auth")
