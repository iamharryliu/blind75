from collections import Counter
import heapq
from typing import Deque, List


class Solution:
    @classmethod
    def leastInterval(self, tasks: List[str], n: int) -> int:
        available_tasks = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(available_tasks)

        time = 0
        unavailable_tasks = Deque()

        while available_tasks or unavailable_tasks:
            time += 1

            # pop tasks from available and add to unavailable if the count is not
            if available_tasks:
                count = heapq.heappop(available_tasks) + 1
                if count:
                    unavailable_tasks.append([count, time + n])

            # Shift task back to available heap
            if unavailable_tasks and unavailable_tasks[0][1] == time:
                heapq.heappush(available_tasks, unavailable_tasks.popleft()[0])
        return time


res = Solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2)
print(res == 8)
