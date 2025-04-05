#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root]
        result = []

        while stack:
            stack_current_level = stack
            stack = []
            current_level_vals = []
            for node in stack_current_level:
                if node is None:
                    continue
                current_level_vals.append(node.val)
                stack.extend([node.left, node.right])
            if len(current_level_vals) > 0:
                result.append(current_level_vals)
            
        return result

# @lc code=end

