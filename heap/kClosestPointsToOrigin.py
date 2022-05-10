from typing import List
import heapq


class Solution:
    @classmethod
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (x**2 + y**2, [x, y]))
        return [heapq.heappop(heap)[1] for _ in range(k)]


print(Solution.kClosest(points=[[1, 3], [-2, 2]], k=1) == [[-2, 2]])
