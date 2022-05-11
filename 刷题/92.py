from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_node = ListNode(val=-1)
        dummy_node.next = head
        pre = dummy_node
        for i in range(left - 1):
            pre = pre.next

        right_node = pre
        for i in range(right - left + 1):
            right_node = right_node.next

        left_node = pre.next
        cur_node = right_node.next

        pre.next = None
        right_node.next = None
        self.reverse_linked_list(left_node)

        pre.next = right_node
        left_node.next = cur_node

        return dummy_node.next

    def reverse_linked_list(self, head):
        if not head or not head.next:
            return head

        new_head = self.reverse_linked_list(head.next)
        head.next.next = head
        head.next = None

        return new_head
