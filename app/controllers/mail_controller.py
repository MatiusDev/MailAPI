from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models.mail import Mail

from app.services.mail.mail_service import post

router = APIRouter()

@router.post("/sendmail")
async def send_email(mail: Mail):
  content = await post(mail)
  if content["status"] == "fail":
    return JSONResponse(content=content, status_code=500)
  return JSONResponse(content=content, status_code=200)