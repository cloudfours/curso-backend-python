from typing import List
from fastapi import Depends, FastAPI, Body, Path, Query, HTTPException
from middlaware.error_handler import Errorhandler
from apps.movies import appRouter
from security.login import appRouterLogin
app = FastAPI()
app.title = "mi app con fastApi"
app.version = "2.5"
app.add_middleware(Errorhandler)
app.include_router(appRouterLogin)

app.include_router(appRouter)
