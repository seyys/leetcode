#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @functools.cache
        def dfs(n: int):
            if n == 0 or n == 1:
                return self.cost[n]
            return self.cost[n] + min(dfs(n-1), dfs(n-2))
        
        self.cost = cost
        self.cost.append(0)
        return dfs(len(cost) - 1)
# @lc code=end

