from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # DFS
        # res = []
        # def dfs(node, currentLevel):
        #     nonlocal res
        #     if not node: return
        #     if currentLevel >= len(res):
        #         res.append(node.val)
        #     if node.right:
        #         dfs(node.right, currentLevel+1)
        #     if node.left:
        #         dfs(node.left, currentLevel+1)

        # dfs(root, 0)
        # return res

        # BFS
        res = []
        q = deque([root])
        while root and q:
            res.append(q[-1].val)
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
