#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        result = 0
        left = 0
        right = 0
        while right < len(nums):
            prev = 1
            while right < len(nums) and nums[right] != 0:
                prev *= nums[right]
                result = max(result, prev)
                right += 1
            while left + 1 < right:
                prev //= nums[left]
                result = max(result, prev)
                left += 1
            right += 1
            left = right
        return result
        
# @lc code=end

