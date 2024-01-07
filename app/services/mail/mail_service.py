import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.models.mail import Mail

from .mail_config_service import get_mail_config

async def post(mail: Mail):
  try:
    mail_config = get_mail_config()
    
    msg = MIMEMultipart()
    msg['From'] = mail.email
    msg['To'] = mail_config["destination_mail"]
    msg['Subject'] = f'Portafolio: Nuevo mensaje de {mail.name} - {mail.email}'
    msg_text = MIMEText(mail.message, 'plain')    
    msg.attach(msg_text)
    
    await aiosmtplib.send(
      msg, 
      hostname=mail_config["smtp_server"], 
      port=mail_config["smtp_port"], 
      username=mail_config["smtp_user"],
      password=mail_config["smtp_password"],
      use_tls=False,
    )
    return { "msg": "Su mensaje ha sido enviado correctamente", "status": "ok" }
  except Exception as e:
    print(str(e))
    return { "error": "Hubo un error en el sistema", "status": "fail" }