import re
from dataclasses import dataclass

from library_catalog.domain.common.value_objects import BaseValueObject
from library_catalog.domain.common.exceptions import DomainError


AUTHOR_NO_DIGITS = r"^\D+$"
MAX_AUTHOR_SIZE=50


@dataclass(eq=False)
class WrongAuthorValueError(ValueError, DomainError):
    title: str
    text: str

    @property
    def title(self) -> str:
        return self.text


class EmptyAuthorError(WrongAuthorValueError):
    pass


class TooLongAuthorError(WrongAuthorValueError):
    pass



class Author(BaseValueObject):
    author_name:str
    def _validate(self) -> None:
        if len(self.author_name)=0:



