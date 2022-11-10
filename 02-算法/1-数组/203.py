# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 时间复杂度： O(n)
# 空间复杂度: O(1)
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        tmp = dummy

        while tmp.next is not None:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next

        return dummy.next
