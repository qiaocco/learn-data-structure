# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        q = [root]

        while len(q) > 0:
            size = len(q)
            lst = []
            while size > 0:
                cur = q.pop(0)
                lst.append(cur.val)

                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)

                size -= 1
            result.append(lst[:])

        return result
