import pytest
from quick_python.dict_ops import DictOperations

dsub = DictOperations()
data = {"a": 1, "c": 3}


class TestDictOperations:
    def test_get_item_using_get_method(self):
        assert dsub.get(data, "a") == 1
        assert dsub.get(data, "b") == None

    def test_get_by_index_raises_KeyError_when_key_doesnot_exist(self):
        with pytest.raises(KeyError):
            assert dsub.get_by_index(data, "x")

    def test_get_by_index_with_existing_key(self):
        assert dsub.get_by_index(data, "a") == 1

    def test_set_value_on_dictionary(self):
        data_copy = data.copy()
        dsub.set(data_copy, "b", 2)
        assert dsub.get(data_copy, "b") == 2

    def test_set_update_value_for_existing_key(self):
        data_copy = data.copy()
        dsub.set(data_copy, "a", 5)
        assert dsub.get_by_index(data_copy, "a") == 5

    def test_has_key_in_a_dictionary(self):
        assert dsub.has_key(data, "f") == False
        assert dsub.has_key(data, "a") == True

    def test_create_from_tuples(self):
        assert dsub.create_from_tuples([("a", 1), ("b", 2)]) == {"a": 1, "b": 2}

    def test_keys(self):
        assert list(dsub.get_keys(data)) == ["a", "c"]

    # dict.values returns an Iterable, list acts on an Iterable
    # and converts it to a list.
    # Reference: https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html
    def test_values(self):
        assert list(dsub.get_values(data)) == [1, 3]

    # when a function does not explicitly return None, asserting
    # that the return value is None does not work. mypy or pytest will
    # fail the test (I hope it's the former)
    def test_remove_key_from_dictionary(self):
        data_copy = data.copy()
        dsub.remove_key(data_copy, "a")
        assert data_copy == {"c": 3}

    def test_remove_non_existant_key_from_dictionary(self):
        data_copy = data.copy()
        with pytest.raises(KeyError):
            dsub.remove_key(data_copy, "q")

    def test_capture_named_args(self):
        captured = dsub.capture_named_args(
            first_name="Jason", last_name="Bourne", location="London"
        )
        assert captured == {
            "first_name": "Jason",
            "last_name": "Bourne",
            "location": "London",
        }
