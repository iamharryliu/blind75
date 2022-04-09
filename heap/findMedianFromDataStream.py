import heapq


class MedianFinder:
    def __init__(self):
        # initialize empty heaps
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # push num into small heap
        heapq.heappush(self.small, -1 * num)

        # if small heap root value is is greater than large heap root value move it to large heap
        if self.small and self.large and not ((self.small[0] * -1) < self.large[0]):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        # small heap is too long
        if len(self.large) + 1 < len(self.small):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        # large heap is too long
        if len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large) * -1
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        # return small heap root if small heap is longer
        if len(self.large) < len(self.small):
            return self.small[0] * -1

        # return small heap root if large heap is longer
        if len(self.small) < len(self.large):
            return self.large[0]

        # return median
        return (-1 * self.small[0] + self.large[0]) / 2


commands = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
nums = [[], [1], [2], [], [3], []]
for i, command in enumerate(commands):
    if command == "MedianFinder":
        obj = MedianFinder()
    if command == "addNum":
        obj.addNum(nums[i][0])
    if command == "findMedian":
        print(obj.findMedian())
