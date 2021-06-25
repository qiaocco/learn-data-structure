# 参考
# https://leetcode-cn.com/problems/design-hashset/solution/xiang-jie-hashset-de-she-ji-zai-shi-jian-4plc/

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def add(self, key: int) -> None:
        hashkey = self.hash(key)
        if key in self.table[hashkey]:
            return
        self.table[hashkey].append(key)

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        if key not in self.table[hashkey]:
            return
        self.table[hashkey].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashkey = self.hash(key)
        return key in self.table[hashkey]


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
obj.add(3)
print(obj.table)
obj.remove(1)
print(obj.table)
# print(obj._items)
#
# param_3 = obj.contains(1)
# print(param_3)
