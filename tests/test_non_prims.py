import pytest
from quick_python.non_prims import (
    ListOperations,
    TupleOperations,
    SetOperations,
)

lsub = ListOperations()
tsub = TupleOperations()
set_sub = SetOperations()


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


set_data = set(["angie", "laura", "kate", "bella"])


class TestSetOperations:
    def test_create_set_using_list(self):
        assert set_sub.create(
            ["angie", "laura", "kate", "bella", "laura", "kate"]
        ) == set(
            [
                "angie",
                "laura",
                "kate",
                "bella",
            ]
        )

    def test_has_item_in_set(self):
        assert set_sub.has(set_data, "kate") == True
        assert set_sub.has(set_data, "jenna") == False

    def test_set_union_should_have_all_items(self):
        data_a = set([1, 2, 3])
        data_b = set([3, 5, 7, 2])
        assert set_sub.union(data_a, data_b) == set([1, 2, 3, 5, 7, 2])

    def test_add_item_that_already_exists_to_set(self):
        set_data_copy = set_data.copy()
        set_sub.add_item(set_data_copy, "kate")
        assert set_data_copy == set_data

    def test_add_new_item_to_set(self):
        set_data_copy = set_data.copy()
        set_sub.add_item(set_data_copy, "marie")
        assert set_data_copy == set(["angie", "laura", "kate", "bella", "marie"])

    def test_add_multiple_values_to_set(self):
        set_data_copy = set_data.copy()
        set_sub.add_items(set_data_copy, ["kate", "angie", "jessica"])
        assert set_data_copy == set(["angie", "laura", "kate", "bella", "jessica"])

    def test_set_intersection_should_have_common_items(self):
        data_a = set([1, 2, 3])
        data_b = set([3, 5, 7, 2])
        assert set_sub.intersection(data_a, data_b) == set([2, 3])

    def test_set_difference_with_values_in_a_but_not_in_b(self):
        data_a = set([1, 2, 3])
        data_b = set([3, 5, 7, 2])
        assert set_sub.difference(data_a, data_b) == set([1])
        assert set_sub.difference(data_b, data_a) == set([5, 7])

    def test_length_of_set(self):
        assert set_sub.set_length(set_data) == 4

    def test_symmetric_difference_must_exclude_all_values_in_both(self):
        data_a = set([1, 2, 3])
        data_b = set([3, 5, 7, 2])
        assert set_sub.symmetric_difference(data_a, data_b) == set([1, 5, 7])

    def test_a_is_not_subset_of_b(self):
        data_a = set([1, 2, 3])
        data_b = set([1, 3, 5, 7, 2])
        assert set_sub.is_subset(data_b, data_a) == False

    def test_a_is_subset_of_b(self):
        data_a = set([1, 2, 3])
        data_b = set([1, 3, 5, 7, 2])
        assert set_sub.is_subset(data_a, data_b) == True

    def test_a_is_superset_of_b(self):
        data_a = set([1, 2, 3])
        data_b = set([1, 3, 5, 7, 2])
        assert set_sub.is_superset(data_b, data_a) == True

    def test_a_is_not_superset_of_b(self):
        data_a = set([1, 2, 3])
        data_b = set([1, 3, 5, 7, 2])
        assert set_sub.is_superset(data_a, data_b) == False
