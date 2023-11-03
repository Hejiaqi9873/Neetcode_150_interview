# 19. Remove Nth Node From End of List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        left_pointer = dummy_node
        right_pointer = head

        # make the right pointer into the head + n position
        while n > 0 and right_pointer:
            right_pointer = right_pointer.next
            n -= 1

        # move both left and right pointer, and end situation is right_pointer is null
        while right_pointer:
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next

        # delete
        left_pointer.next = left_pointer.next.next

        return dummy_node.next

if __name__ == "__main__":
    head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    solution = Solution().removeNthFromEnd(head=head, n = 1)
    cur = solution
    while cur:
        print(cur.val)
        cur = cur.next