#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0
            return max(dfs(root.left), dfs(root.right)) + 1
            
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node is None:
                continue
            depth_diff = dfs(node.left) - dfs(node.right)
            if depth_diff < -1 or depth_diff > 1:
                return False
            stack.extend([node.left, node.right])
        return True

# @lc code=end

