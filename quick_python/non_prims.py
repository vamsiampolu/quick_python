"""Operations on non primitives such as List, Tuple and Dictionary"""
from typing import TypeVar

T = TypeVar("T")


class ListOperations:
    def get(self, a: list[T], n: int) -> T:
        return a[n]

    def list_length(self, a: list[T]) -> int:
        return len(a)

    def list_slice(self, a: list[T], start: int, end: int) -> list[T]:
        return a[start:end]

    def list_delete_element(self, a: list[T], n: int) -> list[T]:
        del a[n]
        return a

    def list_append(self, a: list[T], value: T) -> list[T]:
        a.append(value)
        return a

    def list_insert_at_index(self, a: list[T], n: int, value: T) -> list[T]:
        a.insert(n, value)
        return a

    def list_pop(self, a: list[T]) -> list[T]:
        return a.pop()

    def list_splice(self, a: list[T], start: int, end: int, b: list[T]) -> list[T]:
        a[start:end] = b
        return a
