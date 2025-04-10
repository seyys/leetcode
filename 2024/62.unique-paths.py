#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                return 1
            if x >= m or y >= n:
                return 0
            if memo[x][y] > 0:
                return memo[x][y]
            result = dfs(x+1, y) + dfs(x, y+1)
            memo[x][y] = result
            return result
        return dfs(0,0)
        
# @lc code=end

