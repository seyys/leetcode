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
        root = TreeNode()
        stack = [root]
        inorder_seen_indices = set([-1, len(preorder)])

        inorder_hash = {}
        for i, val in enumerate(inorder):
            inorder_hash[val] = i
        
        for i, val in enumerate(preorder):
            node = stack.pop()
            node.val = val
            inorder_seen_indices.add(inorder_hash[val])
            if inorder_hash[val] + 1 not in inorder_seen_indices:
                node.right = TreeNode()
                stack.append(node.right)
            if inorder_hash[val] - 1 not in inorder_seen_indices:
                node.left = TreeNode()
                stack.append(node.left)

        return root
# @lc code=end

