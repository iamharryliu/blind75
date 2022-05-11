# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root):
        q = [root]
        res = []

        while q:
            newQ = []
            for node in q:
                if node.left:
                    newQ.append(node.left)
                if node.right:
                    newQ.append(node.right)
            res.append([n.val for n in q])
            q = newQ

        return res
