class Solution:
    @classmethod
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0

        def dfs(grid, x, y):
            if (
                x < 0
                or y < 0
                or x >= len(grid)
                or y >= len(grid[0])
                or grid[x][y] != "1"
            ):
                return
            grid[x][y] = "#"
            dfs(grid, x + 1, y)
            dfs(grid, x - 1, y)
            dfs(grid, x, y + 1)
            dfs(grid, x, y - 1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    dfs(grid, x, y)
                    count += 1
        return count


res = Solution.numIslands(
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
)
print(res)
