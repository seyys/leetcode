#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        wall = []
        vol = 0
        for i in range(1,len(height)):
            if height[i] < height[i-1]:
                wall.append((height[i-1], height[i], i-1))
            else:
                while len(wall) > 0:
                    last_wall = wall.pop()
                    vol += (min(height[i], last_wall[0]) - last_wall[1]) * (i - last_wall[2] - 1) 
                    if height[i] < last_wall[0]:
                        wall.append((last_wall[0], height[i], last_wall[2]))
                        break
        return vol
# @lc code=end

