"""Operations on integer and string primitives"""
from typing import Any


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


class BoolOperators:
    def is_truthy(self, a: Any):
        if a:
            return True
        else:
            return False
