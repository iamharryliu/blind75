# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @classmethod
    def removeNthFromEnd(self, head, n):
        slow = fast = head

        # advance fast n nodes
        for _ in range(n):
            fast = fast.next

        # this covers the case of [] -> None, [n] -> None, [n1, n2]
        if not fast:
            return head.next

        # advance fast and slow nodes
        while fast.next:
            fast = fast.next
            slow = slow.next

        # skip n node
        slow.next = slow.next.next

        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node4.next = node5
node3.next = node4
node2.next = node3
node1.next = node2
head = node1

result = Solution.removeNthFromEnd(head, 2)
while result:
    print(result.val)
    result = result.next
