#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_leaf(node):
            if node.left == None and node.right == None:
                return True
            return False

        if root is None:
            return False

        stack = [root]
        sum_stack = [targetSum]
        while len(stack) > 0:
            node = stack.pop()
            ssum = sum_stack.pop()
            if node is None:
                continue
            if is_leaf(node) and ssum == node.val:
                return True
            stack.extend([node.left, node.right])
            sum_stack.extend([ssum - node.val, ssum - node.val])
        return False

# @lc code=end

