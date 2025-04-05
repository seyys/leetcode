#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_product = len(nums) * [0]
        backward_product = len(nums) * [0]
        result = len(nums) * [0]

        current_product = 1
        for i in range(len(nums)):
            current_product *= nums[i]
            forward_product[i] = current_product

        current_product = 1
        for i in range(len(nums) - 1, -1, -1):
            current_product *= nums[i]
            backward_product[i] = current_product

        forward_product.append(1)
        backward_product.append(1)
        for i in range(len(nums)):
            result[i] = forward_product[i-1] * backward_product[i+1]
            
        return result
# @lc code=end

