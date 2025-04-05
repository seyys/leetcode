#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_height = 0
        while left < right:
            max_height = max(max_height, (right - left) * min(height[left], height[right]))
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return max_height
# @lc code=end

