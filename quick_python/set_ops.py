"""Operations on Set types"""
from typing import TypeVar, Union, Any

T = TypeVar("T")


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
