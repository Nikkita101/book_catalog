from dataclasses import dataclass
from typing import ClassVar
from datetime import datetime
from library_catalog.domain.common.int_vo import IntVO
from library_catalog.domain.common.validation import LimitDigitRule

@dataclass(frozen=True)
class PublishYear(IntVO):
    publish_year: int

    _attr: ClassVar[str] = "publish_year"
    _name: ClassVar[str] = "publish_year"
    _positive = True

    def _validate(self) -> None:
        super()._validate()
        LimitDigitRule(
            digit=self.publish_year,
            limit_digit=datetime.now().year,
            digit_name=self._name,
        )
