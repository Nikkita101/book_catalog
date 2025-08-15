from dataclasses import dataclass
from library_catalog.domain.common.str_vo import StrVO
from typing import ClassVar

MAX_TITLE_SIZE=50



@dataclass(frozen=True)
class Title(StrVO):
    title: str
    _attr: ClassVar[str] = "title"
    _name: ClassVar[str] = "Title"
    _max_len: ClassVar[int] = MAX_TITLE_SIZE


