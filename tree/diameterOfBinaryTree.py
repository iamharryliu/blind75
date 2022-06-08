from turtle import reset
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return max(left, right) + 1

        dfs(root)
        return res

        # Alternate solution
        if not root:
            return 0

        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))

        left = height(root.left)
        right = height(root.right)

        return max(
            left + right,
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
        )
