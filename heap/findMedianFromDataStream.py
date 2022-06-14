import heapq


class MedianFinder:
    def __init__(self):
        self.s = []
        self.l = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.s, -num)
        if self.s and self.l and -self.s[0] > self.l[0]:
            num = -heapq.heappop(self.s)
            heapq.heappush(self.l, num)
        if len(self.s) - len(self.l) > 1:
            num = -heapq.heappop(self.s)
            heapq.heappush(self.l, num)
        if len(self.l) - len(self.s) > 1:
            num = -heapq.heappop(self.l)
            heapq.heappush(self.s, num)

    def findMedian(self) -> float:
        if len(self.s) > len(self.l):
            return -self.s[0]
        if len(self.l) > len(self.s):
            return self.l[0]
        return (-1 * self.s[0] + self.l[0]) / 2


commands = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
nums = [[], [1], [2], [], [3], []]
for i, command in enumerate(commands):
    if command == "MedianFinder":
        obj = MedianFinder()
    if command == "addNum":
        obj.addNum(nums[i][0])
    if command == "findMedian":
        print(obj.findMedian())
