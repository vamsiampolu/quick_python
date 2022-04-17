import pytest
from quick_python.primitives import IntegerOperations, StringOperations

subject = IntegerOperations()
str_subject = StringOperations()

# Integer Addition tests:
class TestAddIntegers:
    def test_add(self):
        assert subject.add(3, 4) == 7

    def test_add_zero(self):
        assert subject.add(3, 0) == 3

    def test_add_to_zero(self):
        assert subject.add(0, 3) == 3

    def test_add_neg(self):
        assert subject.add(3, -1) == 2


# Integer substraction tests:
class TestSubstractIntegers:
    def test_sub(self):
        assert subject.sub(4, 2) == 2

    def test_sub_zero(self):
        assert subject.sub(4, 0) == 4

    def test_sub_one_neg_num(self):
        assert subject.sub(-4, 2) == -6
        assert subject.sub(4, -2) == 6

    def test_sub_both_neg_num(self):
        assert subject.sub(-4, -2) == -2
        assert subject.sub(-2, -4) == 2


# Integer Multiplication tests:
class TestMultiplicationIntegers:
    def test_mul(self):
        assert subject.mul(2, 3) == 6

    def test_mul_zero(self):
        assert subject.mul(4, 0) == 0

    def test_mul_one(self):
        assert subject.mul(7, 1) == 7

    def test_mul_one_neg_num(self):
        assert subject.mul(-2, 1) == -2

    def test_mul_two_neg_num(self):
        assert subject.mul(-3, -2) == 6


# Integer Division tests:
class TestDivisionIntegers:
    def test_div(self):
        assert subject.div(8, 2) == 4

    def test_div_by_one(self):
        assert subject.div(4, 1) == 4

    def test_div_returns_floor_when_not_exactly_divisible(self):
        assert subject.div(7, 2) == 3

    def test_div_by_zero_raises_error(self):
        with pytest.raises(ZeroDivisionError):
            subject.div(3, 0)


# Integer Modulus tests:
class TestModulusIntegers:
    def test_mod(self):
        assert subject.mod(4, 2) == 0
        assert subject.mod(5, 2) == 1
        assert subject.mod(3, 1) == 0

    def test_mod_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            subject.mod(3, 0)


# String Operations Test:
class TestStringOperations:
    def test_str_single_double_quotes(self):
        data = "foobar"
        data2 = "foobar"
        assert data == data2

    def test_str_triple_quotes(self):
        data = """My
House
My
Rules"""

        data2 = "My\nHouse\nMyRules\n"
        assert len(data) == len(data2)

    def test_str_clone(self):
        assert str_subject.clone("foo") == "foo"

    def test_str_len(self):
        assert str_subject.str_len("foobar") == 6
        assert str_subject.str_len("barter") == 6
        assert str_subject.str_len("""\tmy fire\n""") == 9

    def test_str_concat(self):
        assert str_subject.str_concat("any", "day") == "anyday"
        assert str_subject.str_concat("", "march") == "march"
        assert str_subject.str_concat("the dark knight", "") == "the dark knight"

    def test_str_truthy(self):
        assert str_subject.str_truthy("a") == True
        assert str_subject.str_truthy("") == False

    def test_str_get_char(self):
        assert str_subject.str_get_char("fax", 1) == "a"
        assert str_subject.str_get_char("fax", -2) == "a"

        assert str_subject.str_get_char("fax", 2) == "x"
        assert str_subject.str_get_char("fax", -1) == "x"

    def test_str_slice(self):
        data = "tangerine"
        assert str_subject.slice(data, 1, 6) == "anger"
        assert str_subject.slice(data, 0, -1) == "tangerin"
        assert str_subject.slice(data, -1, 0) == ""

    def test_str_slice_start(self):
        data = "tangerine"
        assert str_subject.slice_only_start(data, 0) == data
        assert str_subject.slice_only_start(data, 3) == "gerine"
        assert str_subject.slice_only_start(data, -4) == "rine"

    def test_str_slice_end(self):
        data = "tangerine"
        assert str_subject.slice_only_end(data, -1) == "tangerin"
        assert str_subject.slice_only_end(data, 0) == ""
        assert str_subject.slice_only_end(data, 4) == "tang"
