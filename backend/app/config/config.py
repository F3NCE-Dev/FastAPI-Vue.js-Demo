from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    FRONTEND_ORIGINS: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost", "http://127.0.0.1"]
    DEBUG_MODE: bool = True

settings = Settings()
