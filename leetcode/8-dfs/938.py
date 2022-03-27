class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        q = []
        q.append(root)
        result = 0
        while len(q) > 0:
            cur = q.pop()
            if low <= cur.val <= high:
                result += cur.val

            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        return result
