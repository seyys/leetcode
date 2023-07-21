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
    result = True
    lastVal = -float('infinity')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def in_order(root):
            if root == None:
                return
            in_order(root.left)
            if root.val <= self.lastVal:
                self.result = False
            self.lastVal = root.val
            in_order(root.right)
        in_order(root)
        return self.result

# @lc code=end

