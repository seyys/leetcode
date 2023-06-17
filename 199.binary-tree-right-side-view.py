#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        result = []
        while q:
            right_val = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    right_val = node.val
                    q.extend([node.left, node.right])
            if right_val != None:
                result.append(right_val)
        return result
        
# @lc code=end

[1,2,4,null,null,3,null]