class Solution:
    @classmethod
    def spiralOrder(self, matrix):
        res = []

        def dfs(r, c):
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] != "#":
                res.append(matrix[r][c])
                matrix[r][c] = "#"

                if c + 1 >= r:
                    dfs(r, c + 1)
                dfs(r + 1, c)
                dfs(r, c - 1)
                dfs(r - 1, c)

        dfs(0, 0)

        return res


test_value = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
result = Solution.spiralOrder(test_value)
print(result == expected)
