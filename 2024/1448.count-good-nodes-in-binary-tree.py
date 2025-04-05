#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, minimum = -float('inf')) -> int:
        if root is None:
            return 0
        new_min = max(root.val, minimum)
        return (1 if root.val >= minimum else 0) + self.goodNodes(root.left, new_min) + self.goodNodes(root.right, new_min)
# @lc code=end

