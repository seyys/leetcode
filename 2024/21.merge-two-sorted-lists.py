#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        node = head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                next = list1.next
                node.next = list1
                list1 = next
            else:
                next = list2.next
                node.next = list2
                list2 = next
            node = node.next
        node.next = list2 if list1 is None else list1
        return head

# @lc code=end

