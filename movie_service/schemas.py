from pydantic import BaseModel
from typing import List, Optional

class MovieIn(BaseModel):
    name: str
    plot: str
    genres: List[str]
    cast_ids: List[int]


class MovieOut(MovieIn):
    id: int


class MovieUpdate(MovieIn):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    cast_ids: Optional[List[int]] = None
