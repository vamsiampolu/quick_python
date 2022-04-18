"""Operations on non primitives such as List, Tuple and Dictionary"""
from typing import TypeVar, Union, Any

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


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

    def list_pop(self, a: list[T]) -> T:
        return a.pop()

    def list_splice(
        self, a: Union[list[T], list[Any]], start: int, end: int, b: list[T]
    ) -> list[T]:
        a[start:end] = b
        return a

    def repeat_value(self, n: T, times: int) -> list[T]:
        return [n] * times

    def repeat_list(self, arr: list[T], times: int) -> list[T]:
        return arr * times


class TupleOperations:
    def empty_tuple(self):
        return ()

    def create_unary_tuple(self, t: T) -> tuple[T]:
        return (t,)

    def create_normal_tuple(self, *args: Any):
        return args


class SetOperations:
    def create(self, data: list[T]) -> set[T]:
        return set(data)

    def has(self, data: set[T], value: T) -> bool:
        return value in data

    def add_item(self, data: set[T], value: T) -> set[T]:
        data.add(value)
        return data

    def add_items(self, data: set[T], values: list[T]) -> set[T]:
        data.update(values)
        return data

    def set_length(self, data: set[T]) -> int:
        return len(data)

    """return a set with items from one or both of the sets"""

    def union(self, data_a: set[T], data_b: set[T]) -> set[T]:
        # can also be written as data_a.union(data_b)
        return data_a | data_b

    def intersection(self, data_a: set[T], data_b: set[T]) -> set[T]:
        # can also be written as data_a.intersection(data_b)
        return data_a & data_b

    def difference(self, data_a: set[T], data_b: set[T]) -> set[T]:
        # can also be written as data_a.difference(data_b)
        return data_a - data_b

    def symmetric_difference(self, data_a: set[T], data_b: set[T]) -> set[T]:
        return data_a ^ data_b

    def is_subset(self, data_a: set[T], data_b: set[T]) -> bool:
        # return data_a.issubset(data_b)
        return data_a <= data_b

    def is_superset(self, data_a: set[T], data_b: set[T]) -> bool:
        return data_a >= data_b
