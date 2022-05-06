from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [root]

        while len(q) > 0:
            size = len(q)
            row = []
            while size > 0:
                data = q.pop(0)
                row.append(data.val)
                size -= 1
                if data.left is not None:
                    q.append(data.left)
                if data.right is not None:
                    q.append(data.right)
            res.append(row[:])

        for idx in range(len(res)):
            if idx % 2 == 1:
                res[idx].reverse()

        return res
