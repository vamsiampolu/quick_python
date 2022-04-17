import pytest
from quick_python.primitives import IntegerOperations, StringOperations, BoolOperators

subject = IntegerOperations()
str_subject = StringOperations()


class TestIntegerOperations:
    def test_add(self):
        assert subject.add(3, 4) == 7

    def test_add_zero(self):
        assert subject.add(3, 0) == 3

    def test_add_to_zero(self):
        assert subject.add(0, 3) == 3

    def test_add_neg(self):
        assert subject.add(3, -1) == 2

    def test_add_both_neg(self):
        assert subject.add(-3, -2) == -5

    def test_add_both_zero(self):
        assert subject.add(0, 0) == 0

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

    def test_div(self):
        assert subject.div(8, 2) == 4

    def test_div_by_one(self):
        assert subject.div(4, 1) == 4

    def test_div_returns_floor_when_not_exactly_divisible(self):
        assert subject.div(7, 2) == 3

    def test_div_by_zero_raises_error(self):
        with pytest.raises(ZeroDivisionError):
            subject.div(3, 0)

    def test_mod(self):
        assert subject.mod(4, 2) == 0
        assert subject.mod(5, 2) == 1
        assert subject.mod(3, 1) == 0

    def test_mod_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            subject.mod(3, 0)

    def test_cast_nonnumber_to_int(self):
        with pytest.raises(ValueError):
            subject.cast_to_int("mega")

    def test_cast_number_to_int(self):
        assert subject.cast_to_int("44") == 44

    def test_cast_float_string_to_int(self):
        with pytest.raises(ValueError):
            subject.cast_to_int("44.234") == 44

    def test_exponentiation_where_exponent_is_zero(self):
        subject.exponentiation(2, 0) == 1

    def test_exponentiation_where_exponent_is_one(self):
        subject.exponentiation(3, 1) == 3

    def test_exponentiation_where_exponent_is_a_positive_integer(self):
        subject.exponentiation(3, 2) == 9

    def test_exponentiation_where_exponent_is_a_negative_number(self):
        subject.exponentiation(3, -1) == 1 / 3

    def test_exponentiation_where_exponent_is_a_fraction(self):
        subject.exponentiation(9, 1 / 2) == 3


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

    def test_str_find_non_existant_sub_string(self):
        assert str_subject.str_find("tangerine", "mandarin") == -1

    def test_str_find_sub_string(self):
        assert str_subject.str_find("tangerine", "anger") == 1

    def test_find_entire_string(self):
        assert str_subject.str_find("tangerine", "tangerine") == 0

    def test_str_index_non_existant_sub_string(self):
        with pytest.raises(ValueError):
            assert str_subject.str_index("tangerine", "grape")

    def test_str_index_sub_string(self):
        assert str_subject.str_index("tangerine", "anger") == 1

    def test_index_entire_string(self):
        assert str_subject.str_index("tangerine", "tangerine") == 0

    def test_cast_to_string(self):
        assert str_subject.cast_to_string(None) == "None"
        assert str_subject.cast_to_string(True) == "True"
        assert str_subject.cast_to_string(1) == "1"
        assert str_subject.cast_to_string(3.5) == "3.5"

    def test_strip_whitespace_when_string_has_only_spaces(self):
        assert str_subject.strip_whitespace("     ") == ""

    def test_strip_whitespace_with_string_that_has_trailing_spaces(self):
        assert str_subject.strip_whitespace("foo bar  ") == "foo bar"
        assert str_subject.strip_whitespace("  foo bar ") == "foo bar"

    def test_str_split_where_substring_does_not_exist(self):
        assert str_subject.str_split("belly up", ",") == ["belly up"]

    def test_str_split_where_substring_is_last_char(self):
        assert str_subject.str_split("any method,", ",") == ["any method", ""]

    def test_str_split_with_substring(self):
        assert str_subject.str_split("37, 41, 43, 47, 53, 59", ", ") == [
            "37",
            "41",
            "43",
            "47",
            "53",
            "59",
        ]


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
