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

        # using deque
        if not root:
            return None
        res = []
        q = deque([root])
        while q:
            res.append([node.val for node in q])
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res
