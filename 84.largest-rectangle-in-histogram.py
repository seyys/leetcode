#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_rect = 0
        rects = []
        for i, h1 in enumerate(heights + [0]):
            if len(rects) == 0:
                rects.append((h1, i))
                continue
            if rects[-1][0] < h1:
                rects.append((h1, i))
                continue
            elif rects[-1][0] == h1:
                continue
            while len(rects) > 0 and rects[-1][0] > h1:
                h0, j = rects.pop()
                largest_rect = max(largest_rect, (i - j) * h0)
            rects.append((h1, j))
        return largest_rect

# @lc code=end

