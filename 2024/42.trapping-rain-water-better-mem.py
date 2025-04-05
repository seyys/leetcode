#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        left = None
        for right in range(1, len(height)):
            # Rising edge
            if height[right] > height[right - 1]:
                floor = height[right - 1]
                if left is None:
                    left = right - 2 
                # Look for falling edge that is higher than current 
                while left >= 0:
                    if height[left] > height[left + 1] and height[left] > floor:
                        vol += (min(height[left], height[right]) - floor) * (right - left - 1)
                        floor = height[left]
                    if height[left] >= height[right]:
                        break
                    left -= 1
            if height[right] < height[right - 1]:
                left = None
        return vol
# @lc code=end

