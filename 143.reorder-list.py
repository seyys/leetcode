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
        node = head
        l = []
        while node != None:
            l.append(node)
            node = node.next 
        
        node = head
        idx = len(l) - 1
        while node != None and l[idx] != node and node.next != l[idx]:
            foo = node.next
            l[idx-1].next = None
            node.next = l[idx]
            node.next.next = foo
            idx -= 1
            node = node.next.next
        

# @lc code=end

