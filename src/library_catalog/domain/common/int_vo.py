from dataclasses import dataclass
from typing import ClassVar
from library_catalog.domain.common.value_objects import BaseValueObject
from library_catalog.domain.common.validation import PositiveDigitRule

@dataclass(frozen=True)
class IntVO(BaseValueObject):
    _attr: ClassVar[str]
    _name: ClassVar[str]
    _positive: ClassVar[bool] = True

    def _validate(self) -> None:
        value = getattr(self, self._attr)
        if self._positive:
            PositiveDigitRule(digit=value, digit_name=self._name)
