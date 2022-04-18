"""Operations on non primitives such as List, Tuple and Dictionary"""
from typing import TypeVar, Union, Any, Optional, Iterable

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


class DictOperations:
    def get(self, data: dict[K, V], key: K) -> Optional[V]:
        return data.get(key)

    def get_by_index(self, data: dict[K, V], key: K) -> V:
        return data[key]

    # None is the default return value if a function does not return a value.
    def set(self, data: dict[K, V], key: K, value: V) -> None:
        data[key] = value

    def has_key(self, data: dict[K, V], key: K) -> bool:
        return key in data

    def create_from_tuples(self, pairs: list[tuple[K, V]]) -> dict[K, V]:
        return dict(pairs)

    # this is a live list, this list should update whenever a key is added or removed from the dictionary.
    def get_keys(self, data: dict[K, V]) -> Iterable[K]:
        return data.keys()

    def get_values(self, data: dict[K, V]) -> Iterable[V]:
        return data.values()
