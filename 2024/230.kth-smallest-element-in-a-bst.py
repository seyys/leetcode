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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traversal(root):
            if root:
                yield from inorder_traversal(root.left)
                yield root.val
                yield from inorder_traversal(root.right)
        
        gen = inorder_traversal(root)
        for _ in range(k - 1):
            next(gen)
        return next(gen)
        
# @lc code=end

