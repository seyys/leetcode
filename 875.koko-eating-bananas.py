#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 0

        while low < high - 1:
            mid = (high + low) // 2
            t = sum((x - 1) // mid + 1 for x in piles)
            print(low, high, mid, t)
            if t > h:
                low = mid
            else:
                high = mid

        print(low, high)
        return high

# @lc code=end