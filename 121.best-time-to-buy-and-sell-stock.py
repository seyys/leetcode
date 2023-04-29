#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        profit = 0
        for price in prices:
            min_val = min(min_val, price)
            profit = max(profit, price - min_val)
        return profit
# @lc code=end
