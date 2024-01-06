from fastapi import APIRouter
from services.test_service import test_content
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def get():
  content = test_content()
  return JSONResponse(content=content, status_code=200)