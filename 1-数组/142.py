# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode.cn/problems/linked-list-cycle-ii/solutions/441131/huan-xing-lian-biao-ii-by-leetcode-solution/
# 时间复杂度： O(n)
# 空间复杂度： O(n)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node = head
        seen = dict()
        while node is not None:
            if seen.get(node):
                return node
            seen[node] = True
            node = node.next
        return None