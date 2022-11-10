# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 一把过
# 时间复杂度：O(n)
# 空间复杂度： O(n)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = self.swapPairs(head.next.next)
        next_node = head.next
        head.next = new_head
        next_node.next = head
        return next_node