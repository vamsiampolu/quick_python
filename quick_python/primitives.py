"""Operations on integer and string primitives"""


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
