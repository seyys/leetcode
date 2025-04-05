#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sort = sorted(nums)
        result = []
        for i in range(len(nums_sort) - 2):
            if i > 0 and nums_sort[i] == nums_sort[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums_sort[i] + nums_sort[j] + nums_sort[k] == 0:
                    result.append([nums_sort[i], nums_sort[j], nums_sort[k]])
                if nums_sort[i] + nums_sort[j] + nums_sort[k] > 0:
                    k -= 1
                    while j < k and nums_sort[k] == nums_sort[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums_sort[j] == nums_sort[j - 1]:
                        j += 1
        return result
# @lc code=end

