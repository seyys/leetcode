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
from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        queue = deque()

        node = head
        while node is not None:
            queue.append(node)
            node = node.next

        isLeft = True
        node = head
        while len(queue) > 0:
            node.next = queue.popleft() if isLeft else queue.pop()
            node = node.next
            isLeft = not isLeft
        node.next = None

# @lc code=end

