# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @classmethod
    def reorderList(self, head):
        # step 1: find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse second half
        previous, head2 = None, slow.next
        while head2:
            current = head2
            head2 = head2.next
            current.next = previous
            previous = current
        # remove cycle
        slow.next = None

        # #step 3: merge lists
        head1, head2 = head, previous
        while head2:
            nextNode = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextNode


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node4.next = node5
node3.next = node4
node2.next = node3
node1.next = node2

Solution.reorderList(node1)
while node1:
    print(node1.val)
    node1 = node1.next
