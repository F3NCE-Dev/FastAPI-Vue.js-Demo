from pydantic import BaseModel

class StatusResponse(BaseModel):
    success: bool
    detail: str

class TextResponse(BaseModel):
    text: str
