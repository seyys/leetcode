#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_is_subtree(self, root, subRoot):
            tree1 = [root]
            tree2 = [subRoot]
            while tree1 and tree2:
                node1 = tree1.pop()
                node2 = tree2.pop()
                if node1 == None and node2 == None:
                    continue
                if node1 == None or node2 == None:
                    return False
                if node1.val != node2.val:
                    return False
                tree1.extend([node1.left, node1.right])
                tree2.extend([node2.left, node2.right])
            return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        return self.check_is_subtree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
# @lc code=end

