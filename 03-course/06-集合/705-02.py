class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._items = [False] * 1000001

    def add(self, key: int) -> None:
        self._items[key] = True

    def remove(self, key: int) -> None:
        self._items[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self._items[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(1)
# print(obj._items)
# obj.remove(1)
# print(obj._items)
#
# param_3 = obj.contains(1)
# print(param_3)
