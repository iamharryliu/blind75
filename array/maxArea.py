class Solution:
    @classmethod
    def maxArea(self, height):
        left, right, width, maxArea = 0, len(height) - 1, len(height) - 1, 0
        for width in range(width, 0, -1):
            if height[left] <= height[right]:
                maxArea, left = max(maxArea, height[left] * width), left + 1
            else:
                maxArea, right = max(maxArea, height[right] * width), right - 1
        return maxArea


result = Solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
