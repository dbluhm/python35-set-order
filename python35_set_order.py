"""Order sets according to Python 3.5 convention."""


from typing import Any, Sequence, Set


class Python35SetHashTable:
    def __init__(self):
        self.table = []

    def set_add_entry(self, entry):
        pass

    def set_add_key(self, key):
        pass

    def set_insert_key(self, key, hash):
        pass


def python35_set_order(value: Set[Any]) -> Sequence[Any]:
    return list(value)
