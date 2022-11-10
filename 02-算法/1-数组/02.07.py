# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 双指针法
# 时间复杂度： O(m+n)
# 空间复杂度: O(1)
# https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/solutions/621146/cji-hu-shuang-bai-de-dan-ci-bian-li-jie-ups5w/?orderBy=most_votes
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        pa = headA
        pb = headB

        while pa != pb:
            if pa is None:
                pa = headB
            else:
                pa = pa.next

            if pb is None:
                pb = headA
            else:
                pb = pb.next

        return pa