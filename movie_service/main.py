from fastapi import FastAPI

from db import database, metadata, engine
from endpoints import movies
from exceptions import ItemNotFoundException, item_not_found_exception_handler

app = FastAPI()

metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



app.include_router(movies)

app.add_exception_handler(ItemNotFoundException, item_not_found_exception_handler)

