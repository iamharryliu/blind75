from typing import List


class Solution:
    @classmethod
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea, maxWidth = 0, len(height) - 1

        # iteratively squeeze the width choosing to keep the greater height
        for width in range(maxWidth, 0, -1):
            if height[l] <= height[r]:
                maxArea = max(maxArea, height[l] * width)
                l += 1
            else:
                maxArea = max(maxArea, height[r] * width)
                r -= 1
        return maxArea


result = Solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
