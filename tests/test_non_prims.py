from quick_python.non_prims import ListOperations

lsub = ListOperations()


class TestListOperations:
    def test_lsub_get_item_at_index(self):
        assert lsub.get(["abc", "def"], 0) == "abc"

    def test_lsub_get_item_at_neg_index(self):
        assert lsub.get(["abc", "def"], -1) == "def"

    def test_length_of_list(self):
        assert lsub.list_length([1, 2, 3]) == 3
