import pytest
from quick_python.bool_ops import BoolOperators


class TestBoolOperators:
    def test_falsy_values(self):
        b = BoolOperators()
        assert b.is_truthy(None) == False
        assert b.is_truthy(0) == False
        assert b.is_truthy("") == False
        assert b.is_truthy(False) == False
        assert b.is_truthy({}) == False
        assert b.is_truthy([]) == False
        assert b.is_truthy(()) == False

    def test_truthy_values(self):
        b = BoolOperators()
        assert b.is_truthy(True) == True
        assert b.is_truthy(1) == True
        assert b.is_truthy("a") == True
        assert b.is_truthy([2, 3]) == True
        assert b.is_truthy((5,)) == True
        assert b.is_truthy({"a": "3", "b": "2"}) == True
