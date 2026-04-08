from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.config import settings
from app.schemas.response import StatusResponse
from app.database import setup_database
from contextlib import asynccontextmanager

from app.routers import text, click, user

@asynccontextmanager
async def lifespan(app: FastAPI):
    await setup_database()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.FRONTEND_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(text.router)
app.include_router(click.router)
app.include_router(user.router)

@app.get("/health", tags=["Health Check"], response_model=StatusResponse)
def health_check():
    return {"success": True, "detail": "API is healthy and running"}
