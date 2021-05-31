from collections import deque

linkedlist = deque()

# 添加元素 O(1)
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
print(linkedlist)

# insert O(N)
linkedlist.insert(2, 99)
print(linkedlist)

# access O(N)
print(linkedlist[2])