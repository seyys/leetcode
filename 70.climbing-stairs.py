#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        oneStep = 1
        twoSteps = 2
        for _ in range(n-2):
            foo = oneStep + twoSteps
            oneStep = [twoSteps][0]
            twoSteps = [foo][0]
        return twoSteps
# @lc code=end

