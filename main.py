from fastapi import FastAPI
from app.schemas.url import *
from typing_extensions import Annotated
from app.routers.url import *

app = FastAPI(
    title="URL Shortener",
    description="A simple URL shortener",
    version="0.1.0"
)

app.include_router(router)