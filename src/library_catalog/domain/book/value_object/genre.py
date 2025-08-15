from dataclasses import dataclass
from library_catalog.domain.common.str_vo import StrVO
from typing import ClassVar

MAX_GENRE_SIZE=50





@dataclass(frozen=True)
class Genre(StrVO):
    genre: str
    _attr: ClassVar[str] = "genre"
    _name: ClassVar[str] = "Genre"
    _max_len: ClassVar[int] = MAX_GENRE_SIZE




