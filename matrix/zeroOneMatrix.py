from collections import deque
from typing import List


class Solution:
    @classmethod
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))

        while q:
            r, c = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for x, y in directions:
                nR = r + x
                nC = c + y
                if (
                    0 <= nR < len(mat)
                    and 0 <= nC < len(mat[0])
                    and (nR, nC) not in visited
                ):
                    visited.add((nR, nC))
                    q.append((nR, nC))
                    mat[nR][nC] = mat[r][c] + 1
        return mat


mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
expected_res = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
res = Solution.updateMatrix(mat) == expected_res
print(res)
