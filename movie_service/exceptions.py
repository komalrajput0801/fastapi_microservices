from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


class ItemNotFoundException(Exception):
	def __init__(self, name: str):
		self.name = name



async def item_not_found_exception_handler(request, exc):
	return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"{exc.name} could not be found"},
    )
