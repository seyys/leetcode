#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.cache
        def dfs(amount):
            if amount == 0:
                return 0
            
            min_coins = float('inf')
            for coin_amount in self.coins:
                if amount - coin_amount >= 0:
                    coins = dfs(amount - coin_amount)
                    min_coins = min(coins + 1, min_coins)
            return min_coins
        
        self.coins = coins
        coins = dfs(amount)
        return coins if coins < float('inf') else -1
# @lc code=end

