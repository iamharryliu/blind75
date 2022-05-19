from typing import List


class Solution:
    @classmethod
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh = 0
        time = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        while rotten:
            new_rotten = []
            for r, c in rotten:
                for x, y in directions:
                    nr = r + x
                    nc = c + y
                    if (
                        0 <= nr < len(grid)
                        and 0 <= nc < len(grid[0])
                        and grid[nr][nc] == 1
                    ):
                        new_rotten.append((nr, nc))
                        grid[nr][nc] = 2
            rotten = new_rotten
            if rotten:
                time += 1
                fresh -= len(rotten)
        return time if fresh == 0 else -1


res = Solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(res == 4)

res = Solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
print(res == -1)

res = Solution.orangesRotting([[0, 2]])
print(res == 0)

res = Solution.orangesRotting([[1, 2]])
print(res == 1)
