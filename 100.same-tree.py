#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is None):
            return True
        elif (p is None or q is None):
            return False
        stack1 = [p]
        stack2 = [q]
        while (len(stack1) > 0 and len(stack2) > 0):
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1 is None and node2 is None:
                continue
            elif (node1 is None or node2 is None):
                return False
            if node1.val != node2.val:
                return False
            stack1.extend([node1.left, node1.right])
            stack2.extend([node2.left, node2.right])
        return True
# @lc code=end

