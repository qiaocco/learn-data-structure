# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 时间复杂度：O(n)，其中 n 是链表的长度。需要对链表的每个节点进行反转操作。
# 空间复杂度：O(n)，其中 n 是链表的长度。空间复杂度主要取决于递归调用的栈空间，最多为 n 层。
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head =  self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head