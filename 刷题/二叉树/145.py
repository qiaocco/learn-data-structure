# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack, res = [], []
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
