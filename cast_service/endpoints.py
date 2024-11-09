from typing import List
from fastapi import Header, APIRouter
from exceptions import ItemNotFoundException
from schemas import CastIn, CastOut
import db_manager

casts = APIRouter(prefix="/api/v1/casts")

@casts.post('/', status_code=201)
async def add_cast(payload: CastIn):
    cast_id = await db_manager.add_cast(payload)
    response = {
        'id': cast_id,
        **payload.dict()
    }

    return response


@casts.get("/{id}", response_model=CastOut)
async def get_cast_by_id(id: int):
    cast = await db_manager.get_cast(id)
    if not cast:
        raise ItemNotFoundException(name="Cast")
    return cast

