from typing import List
from fastapi import Depends, FastAPI, Body, Path, Query, HTTPException
from middlaware.error_handler import Errorhandler
from apps.movies import appRouter
from security.login import appRouterLogin
import uvicorn
import os

app = FastAPI()
app.title = "mi app con fastApi"
app.version = "2.5"
app.add_middleware(Errorhandler)
app.include_router(appRouterLogin)

app.include_router(appRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
                port=int(os.environ.get("PORT", 8000)))
