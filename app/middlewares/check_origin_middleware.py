from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.types import ASGIApp
from starlette.requests import Request
from starlette.responses import Response

class CheckOriginMiddleware(BaseHTTPMiddleware):
  
  def __init__(self, app: ASGIApp, allowed_hosts: set) -> None:
    self.allowed_hosts = allowed_hosts
    super().__init__(app)
  
  async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
    host = request.headers.get("host")
        
    if host not in self.allowed_hosts:
      content = { "error": "Host no permitido", "status": "fail" }
      return JSONResponse(content=content, status_code=401)
    
    response = await call_next(request)
    return response