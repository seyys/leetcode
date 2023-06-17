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
        next_level = [root]
        result = []
        while next_level:
            current_level = next_level
            next_level = []
            level = [node.val for node in current_level if node]
            if level:
                result.append(level)
            for node in current_level:
                if node:
                    next_level.extend([node.left, node.right])
        return result

# @lc code=end

