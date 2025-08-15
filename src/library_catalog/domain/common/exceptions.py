from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=False)
class AppError(Exception):
    """Base Error."""

    status: ClassVar[int] = 500

    @property
    def title(self) -> str:
        return "An app error occurred"


class DomainError(AppError):
    """Base Domain Error."""

    @property
    def title(self) -> str:
        return "A domain error occurred"

class StrError(DomainError):
    """Base Str Error."""

    @property
    def title(self) -> str:
        return "A str error occurred"


@dataclass(eq=False)
class EmptyStrError(StrError):
    str_name:str
    @property
    def title(self) -> str:
        return f"Str <<{self.str_name}>> must be not empty"


@dataclass(eq=False)
class TooLongStrError(StrError):
    str_name:str
    str_size:int
    @property
    def title(self) -> str:
        return f"Str <<{self.str_name}>> is too long. Max len is {self.str_size}"


@dataclass(eq=False)
class DigitInStrError(StrError):
    str_name: str

    @property
    def title(self) -> str:
        return f"Str <<{self.str_name}>> must not include digits"




class CollectionError(DomainError):
    @property
    def title(self) -> str:
        return "A collection error occurred"

@dataclass(eq=False)
class EmptyListError(CollectionError):
    list_name: str

    @property
    def title(self) -> str:
        return f"List <<{self.list_name}>> must be not empty"


class DigitsError(DomainError):
    @property
    def title(self) -> str:
        return "A digits error occurred"

@dataclass(eq=False)
class NotPositiveDigitError(DomainError):
    digit_name:str
    @property
    def title(self) -> str:
        return f"A digit {self.digit_name} must be bigger thar zero."


@dataclass(eq=False)
class MustBeLessError(DigitsError):
    digit_name:str
    limit_digit:int
    @property
    def title(self) -> str:
        return f"A <<{self.digit_name}>> value must be less than {self.limit_digit}"