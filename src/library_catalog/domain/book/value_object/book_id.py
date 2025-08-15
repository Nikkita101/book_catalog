from dataclasses import dataclass
from uuid import UUID

from library_catalog.domain.common.value_objects import ValueObject


@dataclass(frozen=True)
class BookId(ValueObject[UUID]):
    value: UUID
