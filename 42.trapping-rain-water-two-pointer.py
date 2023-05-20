#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0

        while left <= right:
            if max_left < max_right:
                total_water += max(max_left - height[left], 0)
                max_left = max(max_left, height[left])
                left += 1
            else:
                total_water += max(max_right - height[right], 0)
                max_right = max(max_right, height[right])
                right -= 1

        return total_water

# @lc code=end

