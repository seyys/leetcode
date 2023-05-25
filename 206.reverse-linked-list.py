#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
            
        def rev(prev, current):
            if current.next == None:
                current.next = prev
                return current
            foo = current.next
            current.next = prev
            return rev(current, foo)
                
        return rev(None, head)
        
# @lc code=end

