from pydantic import BaseModel
from typing import List, Optional

class CastIn(BaseModel):
    name: str


class CastOut(CastIn):
    id: int
