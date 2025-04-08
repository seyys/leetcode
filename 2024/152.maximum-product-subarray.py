#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def prod(arr):
            result = 1
            for num in arr:
                result *= num
            return result

        # O(n) overall
        def get_max_subarray(subarray):
            if len(subarray) == 1:
                return subarray[0]
            idx_negatives = [i for i, num in enumerate(subarray) if num < 0] # O(n)
            if len(idx_negatives) % 2 == 0:
                return prod(subarray) # O(n)
            return max(prod(subarray[idx_negatives[0]+1:]), prod(subarray[:idx_negatives[-1]])) # O(n)

        if len(nums) == 1:
            return nums[0]
        result = -float('inf')
        zero_indices = [-1] + [i for i, num in enumerate(nums) if num == 0] + [len(nums)] # O(n)
        for i in range(len(zero_indices) - 1): # O(n^2) overall
            subarray = nums[zero_indices[i]+1:zero_indices[i+1]]
            if len(subarray) == 0:
                continue
            result = max(result, get_max_subarray(subarray)) # O(n)

        if result < 0 and len(zero_indices) > 0:
            result = 0

        return result
        
# @lc code=end

