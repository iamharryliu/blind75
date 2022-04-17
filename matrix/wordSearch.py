class Solution:
    @classmethod
    def exist(self, board, word):
        num_rows = len(board)
        num_cols = len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                r < 0
                or c < 0
                or r >= num_rows
                or c >= num_cols
                or (r, c) in visited
                or board[r][c] != word[i]
            ):
                return False
            visited.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            visited.remove((r, c))
            return res

        for r in range(num_rows):
            for c in range(num_cols):
                if dfs(r, c, 0):
                    return True
        return False


matrix = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
result = Solution.exist(matrix, word)
print(result)
