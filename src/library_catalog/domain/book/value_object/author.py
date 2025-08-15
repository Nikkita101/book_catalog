import re
from dataclasses import dataclass
from library_catalog.domain.common.value_objects import BaseValueObject
from typing import List
from typing import ClassVar
from library_catalog.domain.common.str_vo import StrVO
from library_catalog.domain.common.validation import NoDigitsStrRule,NotEmptyListRule

MAX_AUTHOR_SIZE=50




@dataclass(frozen=True)
class Author(StrVO):
    author_name: str

    _attr: ClassVar[str] = "author_name"
    _name: ClassVar[str] = "Author"
    _max_len: ClassVar[int] = MAX_AUTHOR_SIZE

    def _validate(self) -> None:
        super()._validate()  # NotEmpty + MaxLen из StrVO
        NoDigitsStrRule(str_data=self.author_name, str_name=self._name)


class Authors(BaseValueObject):
    authors:List[Author]
    def _validate(self) -> None:
        NotEmptyListRule(list_data=self.authors,list_name="Authors")


