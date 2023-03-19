from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from schema.model import User
from security.jwt_manager import create_token


appRouterLogin=APIRouter()
@appRouterLogin.post('/login', tags=['auth'])
async def login(user: User):
    if (user.email == "admin@gmail.com" and user.password == "admin"):
        token: str = create_token(user.dict())
        return JSONResponse(content=token, status_code=200)
