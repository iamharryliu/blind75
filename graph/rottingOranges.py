from collections import deque
from typing import List


class Solution:
    @classmethod
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        fresh = 0
        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rotten.add((i, j))

        while rotten and fresh > 0:
            newRotten = set()
            for row, col in rotten:
                for x, y in directions:
                    nR = row + x
                    nC = col + y
                    if (
                        0 <= nR < len(grid)
                        and 0 <= nC < len(grid[0])
                        and grid[nR][nC] == 1
                    ):
                        fresh -= 1
                        grid[nR][nC] = 2
                        newRotten.add((nR, nC))
            time += 1
            rotten = newRotten

        return time if not fresh else -1


res = Solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(res == 4)

res = Solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
print(res == -1)

res = Solution.orangesRotting([[0, 2]])
print(res == 0)

res = Solution.orangesRotting([[1, 2]])
print(res == 1)
