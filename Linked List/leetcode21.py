# 21. Merge Two Sorted Lists
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return list1
        elif list1 == None and list2:
            return list2
        elif list1 and list2 == None:
            return list1
        else:
            if list1.val >= list2.val:
                output = ListNode(list2.val)
                cur2 = list2.next
                cur1 = list1
            else:
                output = ListNode(list1.val)
                cur1 = list1.next
                cur2 = list2
            cur = output
            while cur1 or cur2:
                if cur1 and cur2:
                    if cur1.val >= cur2.val:
                        cur.next = ListNode(cur2.val)
                        cur2 = cur2.next
                    else:
                        cur.next = ListNode(cur1.val)
                        cur1 = cur1.next
                elif cur1 and cur2 == None:
                    cur.next = ListNode(cur1.val)
                    cur1 = cur1.next
                elif cur1 == None and cur2:
                    cur.next = ListNode(cur2.val)
                    cur2 = cur2.next
                cur = cur.next


            return output

if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    solution = Solution().mergeTwoLists(list1=list1, list2=list2)
    cur = solution
    while cur:
        print(cur.val)
        cur = cur.next
