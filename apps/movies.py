from typing import List
from fastapi import Depends, FastAPI, Body, Path, Query, HTTPException, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from security.jwt_manager import create_token, JWTbearer
from schema.model import Movie, User
from config.database import Base, Session, engine
from models.movie import Movies as MovieBd
from fastapi.encoders import jsonable_encoder
from middlaware.error_handler import Errorhandler
from services.movieservice import MovieService
appRouter = APIRouter()
Base.metadata.create_all(bind=engine)
# movies = [
#     {
#         'id': 1,
#         'title': 'Avatar',
#         'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
#         'year': '2009',
#         'rating': 7.8,
#         'category': 'Acción'
#     },
#     {
#         'id': 2,
#         'title': 'hulk',
#         'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
#         'year': '2010',
#         'rating': 9.8,
#         'category': 'Terror'
#     }
# ]


@appRouter.get('/hola', tags=['home'])
async def get():
    return HTMLResponse('<h1>hello world</h1>')


@appRouter.get('/movies', tags=['movies'], response_model=List[Movie], status_code=201, dependencies=[Depends(JWTbearer())])
async def movie() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movie()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@appRouter.get('/movies/{id}', tags=['movie'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTbearer())])
async def search_movie(id: int = Path(ge=1, le=2000)) -> List[Movie]:
    bd = Session()
    result = MovieService(bd).get_id_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'no se ha encotrado'})
    return JSONResponse(status_code=201, content=jsonable_encoder(result))


@appRouter.get('/movies/', response_model=List[Movie], dependencies=[Depends(JWTbearer())])
async def get_movie_category(category: str = Query(max_length=15, min_length=5)) -> List[Movie]:
    return buscar(category)


@appRouter.post('/movies/', response_model=dict, status_code=200, dependencies=[Depends(JWTbearer())])
async def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={'message': 'se guardo con exito'})


def buscar(cate: str):
    bd = Session()
    result = MovieService(bd).get_cat_movies(cate)
    if not result:
        return JSONResponse(content={'message': 'no se ha encontrado'}, status_code=404)
    return JSONResponse(status_code=201, content=jsonable_encoder(result))


@appRouter.put('/movies/{id}', tags=['update'], response_model=dict, status_code=200, dependencies=[Depends(JWTbearer())])
async def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).get_id_movie(id)
    if not result:
        return JSONResponse(content={'message': 'no se ha encontrado'}, status_code=404)
    # for movie in movies:
    #     if movie['id'] == id:
    #         movie['title'] = movi.title
    # #         movie['overview'] = movi.overview
    # #         movie['rating'] = movi.rating
    # #         movie['category'] = movi.category
    MovieService(db).update_movie(id, movie)
    return JSONResponse(content={'message': 'se actualizo con exito'}, status_code=200)


@appRouter.delete('/movies/{id}', tags=['movies'], status_code=200, dependencies=[Depends(JWTbearer())])
async def delete_movie(id: int):
    db = Session()
    result=MovieService(db).get_id_movie(id)
    if not result:
        return JSONResponse(content={'message': 'no se ha encontrado'}, status_code=404)
    MovieService(db).delete_movie(id)
    return JSONResponse(content={'message': 'se elimino'}, status_code=200)
