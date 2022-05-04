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

            # dfs base case
            if not root:
                return 0

            # dfs
            left = dfs(root.left)
            right = dfs(root.right)

            # update result
            res = max(res, left + right)

            # return dfs value
            return max(left, right) + 1

        dfs(root)
        return res
