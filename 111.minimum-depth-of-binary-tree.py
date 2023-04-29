#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [root]
        depth_stack = [1]
        while len(stack) > 0:
            node = stack.pop(0)
            depth = depth_stack.pop(0)
            if node is None:
                continue
            if node.left is None and node.right is None:
                return depth
            stack.extend([node.left, node.right])
            depth_stack.extend([depth + 1, depth + 1])
        return 1
# @lc code=end

