# 141. Linked List Cycle
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set_item = set()

        cur = head

        while cur:
            if cur in set_item:
                return True
            set_item.add(cur)
            cur = cur.next
        return False

if __name__ == "__main__":
    head_item = ListNode(3)
    cur1 = ListNode(2)
    head_item.next = cur1
    # head_item.next.next = ListNode(0)
    # head_item.next.next.next = ListNode(4)
    # head_item.next.next.next.next = cur1
    solution = Solution().hasCycle(head_item)
    print(solution)

