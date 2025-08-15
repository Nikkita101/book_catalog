from dataclasses import dataclass
from typing import ClassVar
from library_catalog.domain.common.value_objects import BaseValueObject
from library_catalog.domain.common.validation import NotEmptyStrRule, MaxLenStrRule

@dataclass(frozen=True)
class StrVO(BaseValueObject):
    _attr: ClassVar[str]
    _name: ClassVar[str]
    _max_len: ClassVar[int]

    def _validate(self) -> None:
        value = getattr(self, self._attr)
        NotEmptyStrRule(str_data=value, str_name=self._name)
        MaxLenStrRule(str_data=value, str_name=self._name, max_len=self._max_len)
