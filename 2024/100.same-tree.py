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
        stack_p = [p]
        stack_q = [q]

        while stack_p and stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()

            # Check if both nodes are null, if they are, continue
            if node_p == None and node_q == None:
                continue

            # Check if either node is null, if it is, is not equal
            if node_p == None or node_q == None:
                return False

            # Check if node vals are equal
            if node_p.val != node_q.val:
                return False

            # Add next nodes to stack
            stack_p.extend([node_p.left, node_p.right])
            stack_q.extend([node_q.left, node_q.right])
            
        # If one stack is not empty, are not equal
        if len(stack_p) != len(stack_q):
            return False

        return True

# @lc code=end

