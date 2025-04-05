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
        dummy = ListNode(next=head)
        lead = dummy
        lag = dummy
        for _ in range(n):
            lead = lead.next
        while lead.next is not None:
            lead = lead.next
            lag = lag.next
        lag.next = lag.next.next
        return dummy.next
        
# @lc code=end

