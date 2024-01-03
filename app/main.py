from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
import os

from .models.mail import Mail

load_dotenv()

app = FastAPI()

origins = ["*", "https://matiusdev.github.io/portafolio/"]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
async def get():
  return "Hello World"

@app.post("/sendmail")
async def send_email(mail: Mail):
  try:
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    destination_mail = os.getenv("DESTINATION_MAIL")
    
    msg = MIMEMultipart()
    msg['From'] = mail.email
    msg['To'] = destination_mail
    msg['Subject'] = f'Portafolio: Nuevo mensaje de {mail.name} - {mail.email}'
    msg.attach(MIMEText(mail.message, 'plain'))
    
    with SMTP(smtp_server, smtp_port) as email_server:
      email_server.starttls()
      email_server.login(smtp_user, smtp_password)
      email_server.sendmail(mail.email, destination_mail, msg.as_string())
    return JSONResponse(content={"msg": "El correo fue enviado correctamente", "status": "ok"}, status_code=200)
  except Exception as e:
    return JSONResponse(content={"error": str(e), "status": "fail"}, status_code=500)