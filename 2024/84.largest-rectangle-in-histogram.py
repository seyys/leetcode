#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack_idx = []
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            if len(stack_idx) == 0 or stack_idx[-1][1] < heights[i]:
                stack_idx.append((i, heights[i]))
            else:
                flag = False
                while len(stack_idx) > 0 and stack_idx[-1][1] > heights[i]:
                    flag = True
                    last_idx, last_height = stack_idx.pop()
                    max_area = max(max_area, (i - last_idx) * last_height)
                if flag:
                    stack_idx.append((last_idx, heights[i]))
        return max_area
# @lc code=end

