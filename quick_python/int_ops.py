"""Operations on integers"""
from typing import Union, Any


class IntegerOperations:
    def add(self, a: int, b: int) -> int:
        return a + b

    def sub(self, a: int, b: int) -> int:
        return a - b

    def mul(self, a: int, b: int) -> int:
        return a * b

    def div(self, a: int, b: int) -> int:
        return a // b

    def mod(self, a: int, b: int) -> int:
        return a % b

    def cast_to_int(self, a: str) -> int:
        return int(a)

    def exponentiation(
        self, base: int, exponent: Union[int, float]
    ) -> Union[float, Any]:
        return base**exponent
