#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        @functools.cache
        def dfs(n: int, picked_first):
            if n >= len(nums):
                return 0
            elif n == len(nums)-1 and picked_first:
                return 0
            return max(dfs(n+1, picked_first=False if n == 0 else picked_first), nums[n] + dfs(n+2, picked_first=True if n == 0 else picked_first))

        return dfs(0, False)
        
# @lc code=end

