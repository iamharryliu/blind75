from collections import deque
from typing import List


class Solution:
    @classmethod
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # create q of rotting oranges to begin BFS
        fresh = 0
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                # reduce freshness of adjacent oranges
                for r_direction, c_direction in directions:
                    next_r, next_c = r + r_direction, c + c_direction
                    if (
                        # check for out of bounds
                        next_r < 0
                        or next_c < 0
                        or len(grid) == next_r
                        or len(grid[0]) == next_c
                        # only add to BFS q if cell is a good orange
                        or grid[next_r][next_c] != 1
                    ):
                        continue
                    # turn to bad orange, add to BFS q, decrement fresh
                    grid[next_r][next_c] = 2
                    q.append([next_r, next_c])
                    fresh -= 1

            # increment time each BFS
            time += 1

        # if return -1 if there are still fresh oranges
        return time if fresh == 0 else -1


res = Solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(res == 4)

res = Solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
print(res == -1)

res = Solution.orangesRotting([[0, 2]])
print(res == 0)

res = Solution.orangesRotting([[1, 2]])
print(res == 1)
