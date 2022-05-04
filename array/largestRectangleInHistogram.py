from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i

            # When previous height is smaller , ,
            while stack and stack[-1][1] > h:
                # pop previous value
                previousIndex, previousHeight = stack.pop()
                # calc new res
                res = max(res, previousHeight * (i - previousIndex))
                # change start variable
                start = previousIndex
            stack.append((start, h))

        # compare maxes of values left in stack
        while stack:
            index, height = stack.pop()
            res = max(res, height * (len(heights) - index))

        return res
