"""Operations on integer and string primitives"""
from typing import Union, Any


class FloatOperations:
    def add(self, a: float, b: float) -> float:
        return a + b

    def sub(self, a: float, b: float) -> float:
        return a - b

    def mul(self, a: float, b: float) -> float:
        return a * b

    def div(self, a: float, b: float) -> float:
        return a / b

    def mod(self, a: float, b: float) -> float:
        return a % b

    def cast_to_float(self, a: str) -> float:
        return float(a)


class StringOperations:
    def str_len(self, a: str) -> int:
        return len(a)

    def str_concat(self, a: str, b: str) -> str:
        return a + b

    def str_truthy(self, a: str) -> bool:
        if a:
            return True
        else:
            return False

    def str_get_char(self, a: str, n: int) -> str:
        return a[n]

    # start index is inclusive, end index exclusive
    def slice(self, a: str, start: int, end: int) -> str:
        return a[start:end]

    def clone(self, a: str) -> str:
        return a[:]

    def slice_only_start(self, a: str, start: int) -> str:
        return a[start:]

    def slice_only_end(self, a: str, end: int) -> str:
        return a[:end]

    # get the lowest index of a string using str.find(sub)
    # find takes start and end indices like slice
    def str_find(self, a: str, b: str) -> int:
        return a.find(b)

    # exactly like find but raises a ValueError if substring is not found
    # index takes start and end indices like slice
    def str_index(self, a: str, b: str) -> int:
        return a.index(b)

    def cast_to_string(self, a) -> str:
        return str(a)

    # There are method to strip whitespace from only end of the string:
    # rstrip and lstrip
    def strip_whitespace(self, a: str) -> str:
        # if a string only consists of spaces, the condition will be True
        if a.isspace():
            return ""
        else:
            return a.strip()

    def str_split(self, a: str, sub: str) -> list[str]:
        return a.split(sub)


class BoolOperators:
    def is_truthy(self, a: Any):
        if a:
            return True
        else:
            return False
