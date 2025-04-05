#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_sublist(head: ListNode, k: int):
            dummy = ListNode(0, head)
            curr = head
            prev = None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev, head

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while right is not None:
            for _ in range(k):
                if right is None:
                    return dummy.next
                right = right.next
            start, end = reverse_sublist(left.next, k)        
            left.next = start
            end.next = right
            for _ in range(k):
                left = left.next

        return dummy.next

# @lc code=end

