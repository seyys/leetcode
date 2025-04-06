#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        @functools.cache
        def dfs(n):
            if n >= len(nums):
                return 0
            return max(dfs(n+1), nums[n] + dfs(n+2))
        
        return dfs(0)

# @lc code=end

