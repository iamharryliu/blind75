import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        heap = []
        for ll in lists:
            while ll:
                heapq.heappush(heap, ll.val)

        sortedList = []
        while heap:
            sortedList.append(heapq.heappop(heap))

        root = ListNode(sortedList[0]) if sortedList[0] else None
        if sortedList:
            curr = root
            for num in sortedList[1:]:
                curr.next = ListNode(num)
                curr = curr.next

        return root

