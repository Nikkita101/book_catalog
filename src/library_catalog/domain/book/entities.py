from dataclasses import dataclass
from enum import StrEnum
from uuid import UUID
from library_catalog.domain.book.value_object import Title

class BookStatus(StrEnum):
    IN_STOCK = "in_stock"
    GIVEN_AWAY = "given_away"





@dataclass()
class Book:
    id:UUID
    title:Title
    author: str
    publish_year:int
    genre:str
    total_pages:int
    status:BookStatus