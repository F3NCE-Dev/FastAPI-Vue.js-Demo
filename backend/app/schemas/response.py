from pydantic import BaseModel

class StatusResponse(BaseModel):
    status: str

class TextResponse(BaseModel):
    text: str
