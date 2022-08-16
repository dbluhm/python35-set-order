from python35_set_order import python35_set_order


def test_order():
    value = set([1, 3, 4, 5, 8])
    assert [8, 1, 3, 4, 5] == python35_set_order(value)
