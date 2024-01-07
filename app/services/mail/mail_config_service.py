import os

def get_mail_config():
  return {
    "smtp_server": os.getenv("SMTP_SERVER"),
    "smtp_port": os.getenv("SMTP_PORT"),
    "smtp_user": os.getenv("SMTP_USER"),
    "smtp_password": os.getenv("SMTP_PASSWORD"),
    "destination_mail": os.getenv("DESTINATION_MAIL")
  }