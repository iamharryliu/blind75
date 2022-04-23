from typing import List


class Solution:
    @classmethod
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            width = r-l
            if height[l] < height[r]:
                area = width * height[l]
                l += 1
            else:
                area = width * height[r]
                r -= 1
            maxArea = max(maxArea, area)
        return maxArea


result = Solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
