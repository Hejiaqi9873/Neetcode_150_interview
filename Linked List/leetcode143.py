# 143. Reorder List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # get the second half linked list
        second_half = slow.next
        slow.next = None
        # reverse the second half linked list
        prev, curr = None, second_half
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next


        # reorder head
        cur = head
        se_cur = prev

        while se_cur:
            temp1, temp2 = cur.next, se_cur.next
            cur.next = se_cur
            se_cur.next = temp1
            se_cur = temp2
            cur = temp1

        cur = head
        while cur:
            print(cur.val)
            cur = cur.next
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution = Solution().reorderList(head = head)