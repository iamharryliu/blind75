# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @classmethod
    def reverseList(self, head):
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node3.next = node4
node2.next = node3
node1.next = node2

head = Solution.reverseList(node1)
while head:
    print(head.val)
    head = head.next
