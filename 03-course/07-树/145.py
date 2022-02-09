# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res, stack = list(), list()
        stack.append(root)

        while len(stack) > 0:
            cur = stack.pop()
            res.append(cur.val)

            if cur.left:
                stack.append(cur.left)

            if cur.right:
                stack.append(cur.right)
        res.reverse()
        return res
