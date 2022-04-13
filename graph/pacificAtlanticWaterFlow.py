class Solution:
    @classmethod
    def pacificAtlantic(self, heights):
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(row, col, visited, previousHeight):
            if (
                (row, col) in visited   # already visited
                or row < 0  # out of bound conditions
                or col < 0
                or row == rows
                or col == cols
                or not(heights[row][col] >= previousHeight) # current value is not equal or greater than the previous value
            ):
                return
            # add to visited nodes and dfs adjacent nodes
            visited.add((row, col))
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])

        # loop through first row and last row
        for n in range(rows):
            dfs(n, 0, pacific, heights[n][0])
            dfs(n, cols - 1, atlantic, heights[n][cols - 1])

        # loop through first column and first row
        for n in range(cols):
            dfs(0, n, pacific, heights[0][n])
            dfs(rows - 1, n, atlantic, heights[rows - 1][n])

        # check which values are in both Pacific and Atlantic sets and append to the result
        result = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])
        return result


test_value = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
res = Solution.pacificAtlantic(test_value)
print(res)
