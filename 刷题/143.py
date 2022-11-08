# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lst = []
        node = head
        while node:
            lst.append(node)
            node = node.next

        i = 0
        j = len(lst) - 1
        while i < j:
            lst[i].next = lst[j]
            i += 1
            lst[j].next = lst[i]
            j -= 1
