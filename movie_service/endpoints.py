from typing import List
from fastapi import Header, APIRouter
from exceptions import ItemNotFoundException
from schemas import MovieIn, MovieOut
import db_manager

import httpx

movies = APIRouter(prefix="/movies")

@movies.get('/', response_model=List[MovieOut])
async def index():
    return await db_manager.get_all_movies()

@movies.post('/', status_code=201)
async def add_movie(payload: MovieIn):
    body = payload.dict()
    for cast_id in body.get('cast_ids'):
        r = httpx.get(f'http://localhost:8001/api/v1/casts/{cast_id}')
        if r.status_code == 404:
            raise ItemNotFoundException(name="Cast")

    movie_id = await db_manager.add_movie(payload)
    response = {
        'id': movie_id,
        **payload.dict()
    }

    return response

@movies.put('/{id}')
async def update_movie(id: int, payload: MovieIn):
    movie = payload.dict()
    fake_movie_db[id] = movie
    return None

@movies.put('/{id}')
async def update_movie(id: int, payload: MovieIn):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise ItemNotFoundException(name="Movie")

    update_data = payload.dict(exclude_unset=True)
    movie_in_db = MovieIn(**movie)

    updated_movie = movie_in_db.copy(update=update_data)

    return await db_manager.update_movie(id, updated_movie)

@movies.delete('/{id}')
async def delete_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise ItemNotFoundException(name="Movie")
    return await db_manager.delete_movie(id)
