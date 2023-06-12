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
        dummy = ListNode(0, head)
        subhead, subtail, slow, fast = dummy, head, head, head.next
        tracker = 0
        while True:
            current = subhead
            tracker = 0
            while current and tracker < k:
                current = current.next
                tracker += 1
            if not current:
                break
            for _ in range(k - 1):
                fast.next, slow, fast = slow, fast, fast.next
            subhead.next = slow
            subtail.next = fast
            subhead = subtail
            subtail = fast
            if fast:
                slow, fast = fast, fast.next

        return dummy.next
                
# @lc code=end

