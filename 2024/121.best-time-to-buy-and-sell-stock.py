#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_left = []
        min_val = float('inf')
        for price in prices:
            min_val = min(min_val, price)
            min_left.append(min_val)
        
        max_right = []
        max_val = 0
        for price in reversed(prices):
            max_val = max(max_val, price)
            max_right.append(max_val)
        max_right = reversed(max_right)

        return max(max([y - x for x, y in zip(min_left, max_right)]), 0)
# @lc code=end

