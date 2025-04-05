#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val = float('-inf'), max_val = float('inf')) -> bool:
        if root is None:
            return True
        is_valid = root.val > min_val and root.val < max_val
        return (
            is_valid and 
            self.isValidBST(root.left, min_val, root.val) and 
            self.isValidBST(root.right, root.val, max_val)
        )
# @lc code=end

