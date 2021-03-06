# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):

        # RECURSIVE SOLUTION
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            stack.append(root.val)
            dfs(root.right)

        stack = []
        dfs(root)
        return stack[k - 1]

        # ITERATIVE SOLUTION
        # stack = []
        # while root or stack:
        #     # create stack of nodes on left of subtree (smallest values)
        #     while root:
        #         stack.append(root)
        #         root = root.left

        #     # take nodes from stack and reduce k until k is 0 (nth smallest value)
        #     root = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return root.val
        #     root = root.right
