# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 删除->增加哑结点
# 时间复杂度： O(n)
# 空间复杂度: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_length(head:ListNode):
            length = 0
            while head:
                head = head.next
                length += 1
            return length


        dummy = ListNode(0, head)
        length = get_length(head)

        cur = dummy
        for _ in range(length - n):
            cur = cur.next

        cur.next = cur.next.next
        return dummy.next