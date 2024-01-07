from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.middlewares.check_origin_middleware import CheckOriginMiddleware
from app.middlewares.api_key_middleware import ApiKeyMiddleware

from app.controllers.test_controller import router as test_router
from app.controllers.mail_controller import router as mail_router

load_dotenv()

app = FastAPI()

origins = ["https://matiusdev.github.io", "localhost:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "X-API-KEY"],
)
app.add_middleware(
  CheckOriginMiddleware, 
  allowed_hosts=origins,
)
app.add_middleware(ApiKeyMiddleware)

app.include_router(test_router)
app.include_router(mail_router)