#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = 1
        for num in nums:
            result.append(prefix)
            prefix *= num
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * postfix
            postfix *= nums[i]
        return result
# @lc code=end

