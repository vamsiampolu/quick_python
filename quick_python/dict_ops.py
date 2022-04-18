"""Operations on Dictionaries"""
from typing import TypeVar, Optional, Iterable

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


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

    def remove_key(self, data: dict[K, V], key: K) -> None:
        del data[key]

    def capture_named_args(self, **kwargs):
        return kwargs
