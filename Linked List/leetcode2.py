# 2. Add Two Numbers
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        initial_node = ListNode()
        carry = 0

        cur1, cur2, cur3 = l1, l2, initial_node
        while cur1 or cur2:
            if cur1:
                val1 = cur1.val
            else:
                val1 = 0

            if cur2:
                val2 = cur2.val
            else:
                val2 = 0
            # get the number
            cur_val = val1 + val2 + carry

            carry = cur_val // 10
            # get the number
            cur_val = cur_val % 10
            # update initial_node
            cur3.next = ListNode(cur_val)
            # update cur
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            cur3 = cur3.next
        # check if carry > 1 or not
        if carry > 0:
            cur3.next = ListNode(carry)
        return initial_node.next

if __name__ == "__main__":
    l1_item = ListNode(2)
    l1_item.next = ListNode(4)
    l1_item.next.next = ListNode(3)
    l2_item = ListNode(5)
    l2_item.next = ListNode(6)
    l2_item.next.next = ListNode(4)
    solution = Solution().addTwoNumbers(l1=l1_item, l2=l2_item)
    cur = solution
    while cur:
        print(cur.val)
        cur = cur.next

