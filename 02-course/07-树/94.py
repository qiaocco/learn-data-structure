# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, res = list(), list()
        cur = root

        while cur or len(stack):
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack.pop()
            res.append(node.val)
            cur = node.right
        return res