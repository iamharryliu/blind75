# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        if p and q:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        return p is q

    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        # return false if no node
        if not root:
            return False
        # check current node and tree for match
        if self.isSameTree(root, subRoot):
            return True
        # check if left or right nodes are subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSubtree(self, s, t):
        from hashlib import sha256

        def hashFn(x):
            S = sha256()
            S.update(x)
            return S.hexdigest()

        # merckle node
        def merkle(node):
            if not node:
                return "#"
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hashFn(m_left + str(node.val) + m_right)
            return node.merkle

        # merckle s and t
        merkle(s)
        merkle(t)

        # dfs to check if node merckle matches node merckle
        def dfs(node):
            if not node:
                return False
            return node.merkle == t.merkle or dfs(node.left) or dfs(node.right)

        return dfs(s)
