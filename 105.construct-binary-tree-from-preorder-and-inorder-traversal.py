#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_in = 0
        root = TreeNode()
        stack = [root]
        curr = root
        for pre_node in preorder:
            
            
# @lc code=end

pre 3 9 20 15 7
    ^
in  9 3 15 20 7
      ^