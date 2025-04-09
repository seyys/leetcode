#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums) -> int:
        lis = [-1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                lis[i] = 1
                continue
            
            result = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    result = max(result, 1 + lis[j])
            lis[i] = result

        return max(lis)

# @lc code=end

