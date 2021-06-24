class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._items = []

    def add(self, key: int) -> None:
        if key not in self._items:
            self._items.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self._items.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self._items

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(1)
# print(obj._items)
# obj.remove(1)
# print(obj._items)
#
# param_3 = obj.contains(1)
# print(param_3)