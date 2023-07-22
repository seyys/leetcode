#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    i = 0
    result = None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = k
        def in_order(root):
            if root == None:
                return
            in_order(root.left)
            self.i -= 1
            if self.i == 0:
                self.result = root.val
            elif self.i > 0:
                in_order(root.right)
        in_order(root)
        if self.result == None:
            self.result = 0
        return self.result

# @lc code=end

