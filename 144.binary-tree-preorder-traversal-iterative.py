#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node is None:
                continue
            result.append(node.val)
            stack.extend([node.right, node.left])
        return result

# @lc code=end

