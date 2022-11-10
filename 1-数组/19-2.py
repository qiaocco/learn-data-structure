# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 双指针法，只遍历一次
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solutions/7083/dong-hua-tu-jie-leetcode-di-19-hao-wen-ti-shan-chu/
# 时间复杂度： O(n)
# 空间复杂度: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow, fast = dummy, dummy

        for _ in range(n+1):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next