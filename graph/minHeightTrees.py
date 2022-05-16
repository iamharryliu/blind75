from collections import defaultdict
from typing import List


class Solution:
    @classmethod
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

        leaves = [key for key, val in adj.items() if len(val) == 1]
        new_leaves = leaves

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                new_leaf = adj[leaf][0]
                adj[new_leaf].remove(leaf)
                if len(adj[new_leaf]) == 1:
                    new_leaves.append(new_leaf)
            leaves = new_leaves

        return leaves


print(Solution.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]) == [1])
