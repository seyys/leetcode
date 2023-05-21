#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        minSpeed = high

        while low <= high:
            mid = (high + low) // 2
            t = sum((x - 1) // mid + 1 for x in piles)
            if t > h:
                low = mid + 1
            else:
                minSpeed = min(minSpeed, mid)
                high = mid - 1

        return minSpeed

# @lc code=end