from quick_python.non_prims import ListOperations

lsub = ListOperations()


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
