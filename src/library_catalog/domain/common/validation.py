from dataclasses import dataclass
from abc import ABC, abstractmethod
from exceptions import EmptyStrError, TooLongStrError,DigitInStrError, EmptyListError,NotPositiveDigitError,MustBeLessError

class Rule(ABC):
    @abstractmethod
    def check(self,*args,**kwargs):
        pass



@dataclass(frozen=True)
class NotEmptyStrRule(Rule):
    str_data:str
    str_name:str
    def check(self,*args,**kwargs):
        normalized = "".join(self.str_data.split())
        if not normalized:
            raise EmptyStrError(str_name=self.str_name)

@dataclass(frozen=True)
class MaxLenStrRule(Rule):
    str_data: str
    str_name: str
    max_len: int

    def check(self) -> None:
        if len(self.str_data) > self.max_len:
            raise TooLongStrError(str_name=self.str_name, str_size=self.max_len)

@dataclass(frozen=True)
class NoDigitsStrRule(Rule):
    str_data: str
    str_name: str

    def check(self) -> None:
        if any(ch.isdigit() for ch in self.str_data):
            raise DigitInStrError(str_name=self.str_name)


@dataclass(frozen=True)
class NotEmptyListRule(Rule):
    list_data:list
    list_name:str
    def check(self,*args,**kwargs):
        if len(self.list_data)==0:
            raise EmptyListError(list_name=self.list_name)


@dataclass(frozen=True)
class PositiveDigitRule(Rule):
    digit:int
    digit_name:str
    def check(self,*args,**kwargs):
        if self.digit<=0:
            raise NotPositiveDigitError(digit_name=self.digit_name)



@dataclass(frozen=True)
class LimitDigitRule(Rule):
    digit:int
    limit_digit:int
    digit_name:str
    def check(self,*args,**kwargs):
        if self.digit>self.limit_digit:
            raise MustBeLessError(digit_name=self.digit_name, limit_digit=self.limit_digit)


