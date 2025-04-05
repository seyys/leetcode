#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []

        while stack:
            current_level_stack = stack
            stack = []
            current_level_val = None
            for node in current_level_stack:
                if node is None:
                    continue
                current_level_val = node.val
                stack.extend([node.left, node.right])
            result = result + ([current_level_val] if current_level_val is not None else [])

        return result

# @lc code=end

