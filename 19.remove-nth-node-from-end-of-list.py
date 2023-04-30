#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def removeNth(head, n):
            if head is None:
                return 0
            dep = removeNth(head.next, n) + 1
            if dep == n + 1:
                head.next = head.next.next
            return dep
        if removeNth(head, n) == n:
            head = head.next
        return head
# @lc code=end

