# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 参考：
# https://leetcode.cn/problems/add-two-numbers/solutions/7348/hua-jie-suan-fa-2-liang-shu-xiang-jia-by-guanpengc/
# 时间复杂度： O(max(m, n)), m, n代表两个数组的长度
# 空间复杂度： O(1)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode(0)
        cur = pre

        carry = 0

        while l1 is not None or l2 is not None:
            sum = 0
            if l1 is not None:
                sum += l1.val
            if l2 is not None:
                sum += l2.val
            sum += carry

            carry = sum // 10
            sum = sum % 10

            cur.next = ListNode(sum)
            cur = cur.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry != 0:
            cur.next = ListNode(carry)

        return pre.next
