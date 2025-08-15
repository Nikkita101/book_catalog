# domain/book/value_object/total_pages.py
from dataclasses import dataclass
from typing import ClassVar
from library_catalog.domain.common.int_vo import IntVO

@dataclass(frozen=True)
class TotalPages(IntVO):
    total_pages: int

    _attr: ClassVar[str] = "total_pages"
    _name: ClassVar[str] = "total_pages"
    _positive = True
