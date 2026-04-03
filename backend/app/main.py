from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.config import settings
from app.schemas.response import StatusResponse

from app.routers import text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.FRONTEND_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(text.router)

@app.get("/health", tags=["Health Check"], response_model=StatusResponse)
def health_check():
    return {"status": "ok"}
