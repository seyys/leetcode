#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        node1 = l1
        node2 = l2
        dummy = ListNode()
        result_node = dummy
        while node1 is not None or node2 is not None:
            result_node.next = ListNode()
            result_node = result_node.next
            val = (node1.val if node1 else 0) + (node2.val if node2 else 0) + carry
            result_node.val = val % 10
            carry = val // 10
            node1 = node1.next if node1 else node1
            node2 = node2.next if node2 else node2
        if carry > 0:
            result_node.next = ListNode()
            result_node = result_node.next
            result_node.val = carry
        return dummy.next

# @lc code=end

