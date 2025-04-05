#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = float('inf')
        for price in prices:
            min_buy = min(min_buy, price)
            profit = max(price - min_buy, profit)
        return profit
# @lc code=end

