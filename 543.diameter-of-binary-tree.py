#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(root: Optional[TreeNode]):
            if root == None:
                return 0, 0
            left_depth, left_dia = diameter(root.left)
            right_depth, right_dia = diameter(root.right)
            return max(left_depth + 1, right_depth + 1), max(left_dia, right_dia, left_depth + right_depth)
        _, max_dia = diameter(root)
        return max_dia
        
# @lc code=end

