from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # assigning dummy to start of list in case either are empty
        dum = ListNode()
        tail = dum
        while list1 and list2:
            if list2.val >= list1.val:
                tail.next = list1  # assign next value as list1 node
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # update tail pointer regardless of whats chosen
        # if there are elements still left in either list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dum.next


def print_list(node: Optional[ListNode]):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


s = Solution()
print_list(s.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))),
                           ListNode(1, ListNode(3, ListNode(4)))))
