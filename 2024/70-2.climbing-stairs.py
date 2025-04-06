#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev1 = 1
        prev2 = 2
        result = 0
        for _ in range(n - 2):
            result = prev1 + prev2
            prev1 = prev2
            prev2 = result

        return result
# @lc code=end

