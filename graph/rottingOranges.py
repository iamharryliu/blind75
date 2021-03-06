from collections import deque
from typing import List


class Solution:
    @classmethod
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
                    visited.add((r, c))

        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in directions:
                    nr = r + x
                    nc = c + y
                    if (
                        0 <= nr < len(grid)
                        and 0 <= nc < len(grid[0])
                        and (nr, nc) not in visited
                        and grid[nr][nc] == 1
                    ):
                        visited.add((nr, nc))
                        q.append([nr, nc])
            time += 1
            fresh -= len(q)
        return time if fresh == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
output = 4
res = Solution.orangesRotting(grid)
print(res == output)

grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
output = -1
res = Solution.orangesRotting(grid)
print(res == -1)

grid = [[0, 2]]
output = 0
res = Solution.orangesRotting(grid)
print(res == 0)
