#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            current = dummy
            node1, node2 = l1, l2
            while node1 or node2:
                if not node1:
                    current.next = node2
                    node2 = node2.next
                elif not node2:
                    current.next = node1
                    node1 = node1.next
                elif node1.val < node2.val:
                    current.next = node1
                    node1 = node1.next
                else:
                    current.next = node2
                    node2 = node2.next
                current = current.next
            return dummy.next

        def mergeLists(p, r) -> Optional[ListNode]:
            if p > r:
                return None
            elif r == p:
                return lists[r]
            q = (p + r) // 2
            half1 = mergeLists(p, q)
            half2 = mergeLists(q + 1, r)
            return merge(half1, half2)
        
        return mergeLists(0, len(lists) - 1)

# @lc code=end

