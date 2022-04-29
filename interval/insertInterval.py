from typing import List


class Solution:
    @classmethod
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        res = []

        for i, interval in enumerate(intervals):

            # new interval less than interval
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]

            # new interval greater than interval
            elif interval[1] < newInterval[0]:
                res.append(interval)

            # new interval overlaps current interval
            else:
                newMin = min(newInterval[0], interval[0])
                newMax = max(newInterval[1], interval[1])
                newInterval = [newMin, newMax]

        res.append(newInterval)

        return res


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
res = Solution.insert(intervals, newInterval)
print(res)
print(res == [[1, 5], [6, 9]])

