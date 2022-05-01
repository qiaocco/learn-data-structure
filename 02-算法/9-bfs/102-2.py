from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result

        self.dfs(root, result, 0)
        return result

    def dfs(self, node, result, level):
        if node is None:
            return

        if level > len(result) - 1:
            result.append([])

        result[level].append(node.val)

        if node.left is not None:
            self.dfs(node.left, result, level + 1)
        if node.right is not None:
            self.dfs(node.right, result, level + 1)
