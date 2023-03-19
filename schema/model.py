from typing import Optional
from pydantic import BaseModel, Field
class User(BaseModel):
    email:str
    password:str
class Movie(BaseModel):
    id: int = 0
    title:str | None=Field(max_length=30,min_length=5)
    overview:str | None=Field(max_length=50,min_length=5)
    year:int | None=Field(le=2023, default=2023)
    rating:float | None=Field(gt=1,le=10,default=1)
    category:str | None=Field(max_length=15,min_length=5)
    class Config:
        schema_extra={
            "example":{
                'id':1,
                'title':'nombre de la pelicula',
                'overview':'sipnosis',
                'year':2023,
                'rating':2,
                'category':'la categoria'
            }
        }
