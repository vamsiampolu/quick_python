import pytest
from quick_python.non_prims import (
    ListOperations,
    TupleOperations,
)

lsub = ListOperations()
tsub = TupleOperations()


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
