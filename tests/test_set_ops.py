from quick_python.set_ops import SetOperations

set_sub = SetOperations()
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
