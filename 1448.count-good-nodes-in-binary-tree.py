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
    def goodNodes(self, root: TreeNode) -> int:
        def traverse_tree(node, max_val):
            if node == None:
                return 0
            is_good = 0
            if node.val >= max_val:
                is_good = 1
            return traverse_tree(node.left, max(node.val, max_val)) + traverse_tree(node.right, max(node.val, max_val)) + is_good
        
        return traverse_tree(root, -float('Infinity'))

# @lc code=end

