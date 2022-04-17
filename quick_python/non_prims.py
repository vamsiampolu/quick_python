"""Operations on non primitives such as List, Tuple and Dictionary"""
from typing import TypeVar, Generic

T = TypeVar('T')

class ListOperations:
    def get(self, a: list[T], n: int) -> T:
        return a[n]

    def list_length(self, a: list[T]) -> int:
        return len(a)
