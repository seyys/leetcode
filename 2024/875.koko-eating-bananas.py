#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)
        result = max_speed
        while min_speed <= max_speed:
            k_guess = (max_speed - min_speed) // 2 + min_speed
            t_guess = sum([((x - 1) // k_guess) + 1 for x in piles])
            if t_guess <= h:
                result = k_guess
                max_speed = k_guess - 1
            elif t_guess > h:
                min_speed = k_guess + 1
        return result
# @lc code=end

