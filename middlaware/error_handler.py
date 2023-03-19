from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
class Errorhandler(BaseHTTPMiddleware):
    def __init__(self,app:FastAPI) -> None:
        super().__init__(app)
    async def dispatch(self,request:Request,call_next)->Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return  JSONResponse(status_code=500,content={'message':str(e)})
            
        # return await super().dispatch(request,call_next)
    
    