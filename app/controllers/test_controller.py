from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..services.test_service import get_content

router = APIRouter()

@router.get("/")
async def get():
  content = get_content()
  return JSONResponse(content=content, status_code=200)