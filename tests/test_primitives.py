import pytest
from quick_python.primitives import StringOperations, BoolOperators

str_subject = StringOperations()

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
