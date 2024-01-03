from pydantic import BaseModel

class Mail(BaseModel):
  email: str
  name: str
  message: str