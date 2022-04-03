from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.dfs(root, result, 0)
        result.reverse()
        return result

    def dfs(self, root, result, level):
        if root is None:
            return

        if level > len(result) - 1:
            result.append([])

        result[level].append(root.val)
        if root.left is not None:
            self.dfs(root.left, result, level + 1)
        if root.right is not None:
            self.dfs(root.right, result, level + 1)
