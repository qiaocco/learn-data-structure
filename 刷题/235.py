# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = self.get_path(root, p)
        path_q = self.get_path(root, q)

        ans = None
        for i, j in zip(path_p, path_q):
            if i.val == j.val:
                ans = i
            else:
                break

        return ans

    def get_path(self, root, target):
        node = root
        path = []

        while node != target:
            path.append(node)
            if node.val < target.val:
                node = node.right
            elif node.val > target.val:
                node = node.left
        path.append(node)
        return path
