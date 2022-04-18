import pytest
from quick_python.non_prims import ListOperations, TupleOperations, DictOperations
from collections.abc import KeysView

lsub = ListOperations()
tsub = TupleOperations()
dsub = DictOperations()


class TestListOperations:
    def test_lsub_get_item_at_index(self):
        assert lsub.get(["abc", "def"], 0) == "abc"

    def test_lsub_get_item_at_neg_index(self):
        assert lsub.get(["abc", "def"], -1) == "def"

    def test_length_of_list(self):
        assert lsub.list_length([1, 2, 3]) == 3

    def test_slice_list(self):
        data = [1, 2, 3, 4, 5]
        assert lsub.list_slice(data, 1, 3) == [2, 3]
        assert lsub.list_slice(data, 1, -1) == [2, 3, 4]
        assert lsub.list_slice(data, -1, 0) == []

    def test_delete_element(self):
        data = [1, 2, 3, 4, 5]
        data2 = data.copy()
        assert lsub.list_delete_element(data, 1) == [1, 3, 4, 5]
        assert lsub.list_delete_element(data2, -1) == [1, 2, 3, 4]

    def test_append_element(self):
        data = [1, 2, 3, 4, 5]
        lsub.list_append(data, 6)
        assert data == [1, 2, 3, 4, 5, 6]

    def test_insert_element(self):
        data = [1]
        assert lsub.list_insert_at_index(data, 0, 2) == [2, 1]

    def test_list_pop_on_empty_list(self):
        with pytest.raises(IndexError):
            assert lsub.list_pop([])

    def test_list_pop_on_list(self):
        data = [1, 2, 3, 4]
        assert lsub.list_pop(data) == 4
        assert data == [1, 2, 3]

    def test_splice_empty_list(self):
        assert lsub.list_splice([], 0, 1, [1, 2, 3]) == [1, 2, 3]

    def test_splice_with_list(self):
        assert lsub.list_splice([1, 2, 3], 0, 1, [4, 5]) == [4, 5, 2, 3]

    def test_repeat_element(self):
        assert lsub.repeat_value("money", 3) == ["money", "money", "money"]

    def test_repeat_list(self):
        assert lsub.repeat_list(["hello", "hi", "hey there"], 3) == [
            "hello",
            "hi",
            "hey there",
            "hello",
            "hi",
            "hey there",
            "hello",
            "hi",
            "hey there",
        ]


class TestTupleOperations:
    def test_empty_tuple(self):
        assert tsub.empty_tuple() == ()

    def test_tuple_with_single_element(self):
        assert tsub.create_unary_tuple("fire") == ("fire",)

    def test_rest_args_is_tuple(self):
        assert tsub.create_normal_tuple(1, "foo", True, None) == (1, "foo", True, None)


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
        assert dsub.get_keys(data) == KeysView(["a", "c"])
