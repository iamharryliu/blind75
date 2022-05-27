from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                pi, ph = stack.pop()
                start = pi
                res = max(res, ph * (i - start))
            stack.append((start, h))

        while stack:
            index, height = stack.pop()
            res = max(res, height * (len(heights) - index))

        return res
