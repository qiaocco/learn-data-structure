# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 前序遍历
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack, res = [], []

        while len(stack) > 0 or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left

            root = stack.pop()
            root = root.right
        return res
