from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        initialColor = image[sr][sc]

        def dfs(r, c):
            if (
                0 <= r < len(image)
                and 0 <= c < len(image[0])
                and (r, c) not in visited
                and image[r][c] == initialColor
            ):
                visited.add((r, c))
                image[r][c] = newColor
                for x, y in directions:
                    dfs(r + x, c + y)

        dfs(sr, sc)
        return image
