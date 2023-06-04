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
        node1, node2 = l1, l2
        dummy_result_head = ListNode()
        result_node = dummy_result_head
        while node1 or node2:
            value = 0
            if node1:
                value += node1.val
                node1 = node1.next
            if node2:
                value += node2.val
                node2 = node2.next
            value += carry
            carry = value // 10
            value = value % 10
            result = ListNode(value)
            result_node.next = result
            result_node = result_node.next
        if carry > 0:
            result_node.next = ListNode(carry)

        return dummy_result_head.next

# @lc code=end

