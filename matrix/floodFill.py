from typing import List


class Solution:
    @classmethod
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        visited = set()
        oldColor = image[sr][sc]

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r == len(image)
                or c == len(image[0])
                or image[r][c] != oldColor
                or (r, c) in visited
            ):
                return
            visited.add((r, c))
            image[r][c] = newColor
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image


print(
    Solution.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2)
    == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
)
