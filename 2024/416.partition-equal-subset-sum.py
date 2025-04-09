#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @functools.cache
        def dfs(i, curr_sum):
            if curr_sum < 0:
                return False
            if curr_sum == 0:
                return True
            if i >= len(nums):
                return False
            return dfs(i+1, curr_sum) or dfs(i+1, curr_sum - nums[i])

        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        return dfs(0, target)
        
# @lc code=end

