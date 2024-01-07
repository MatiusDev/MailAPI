from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

import os

class ApiKeyMiddleware(BaseHTTPMiddleware):
  
  async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
    api_key = request.headers.get("X-API-KEY")
    valid_api_key = os.environ.get("GLOBAL_API_KEY")
    
    if not api_key:
      content = { "error": "No has ingresado la API KEY", "status": "fail" }
      return JSONResponse(content=content, status_code=400)
    
    if not valid_api_key:
      content = { "error": "Error con variable API KEY", "status": "fail" }
      return JSONResponse(content=content, status_code=500)
    
    if valid_api_key != api_key:
      content = { "error": "API KEY no válida", "status": "fail" }
      return JSONResponse(content=content, status_code=401)
    
    response = await call_next(request)
    return response