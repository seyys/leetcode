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
        def merge(l1: Optional[ListNode], l2: Optional[ListNode]):
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            dummy = ListNode()
            node = dummy
            while (l1 is not None) or (l2 is not None):
                if l1 is None:
                    node.next = l2
                    break
                elif l2 is None:
                    node.next = l1
                    break
                elif l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            return dummy.next
        
        def merge_lists(lists: List[Optional[ListNode]]):
            match len(lists):
                case 0:
                    return None
                case 1:
                    return lists[0]
                case 2:
                    return merge(lists[0], lists[1])
                case _:
                    mid = len(lists) // 2
                    return merge(merge_lists(lists[:mid]), merge_lists(lists[mid:]))
            
        return merge_lists(lists)

# @lc code=end

