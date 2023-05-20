#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        stack = [] # (pos, max height, min height)

        for right_pos, right_height in enumerate(height):
            while len(stack) > 0:
                left_pos, left_max_height, left_min_height = stack.pop()
                total_water += (min(right_height, left_max_height) - left_min_height) * (right_pos - left_pos - 1)
                if left_max_height > right_height:
                    stack.append((left_pos, left_max_height, right_height))
                    break
            stack.append((right_pos, right_height, 0))
            
        return total_water

# @lc code=end

