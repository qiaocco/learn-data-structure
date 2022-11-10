# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 时间复杂度：O(n)，其中 n 是链表的长度。需要对链表的每个节点进行反转操作。
# 空间复杂度：O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = ListNode(0)

        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre
