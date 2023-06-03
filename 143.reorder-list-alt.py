#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Split list into 2
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        node = slow.next
        foo = None
        while node != None:
            tmp = node.next
            node.next = foo
            foo = node
            node = tmp

        # Merge first and second halves
        first, second = head, foo
        # Break lists
        slow.next = None
        while second != None:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

# @lc code=end

