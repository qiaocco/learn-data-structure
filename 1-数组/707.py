class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# https://leetcode.cn/problems/design-linked-list/solutions/1840997/she-ji-lian-biao-by-leetcode-solution-abix/
class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    # O(index)
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head
        for _ in range(index + 1):
            cur = cur.next

        return cur.val

    # O(1)
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    # O(n)
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    # O(index)
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        index = max(0, index)
        self.size += 1
        to_add = ListNode(val)
        pre = self.head

        for _ in range(index):
            pre = pre.next

        to_add.next = pre.next
        pre.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size or index < 0:
            return

        self.size -= 1
        pre = self.head
        for _ in range(index):
            pre = pre.next

        pre.next = pre.next.next




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)