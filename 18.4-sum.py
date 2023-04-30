#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sum_vals = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_vals == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        break
                    elif sum_vals < target:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    else:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                j += 1
                while j < len(nums) - 2 and nums[j] == nums[j - 1]:
                    j += 1
            i += 1
            while i < len(nums) - 3 and nums[i] == nums[i - 1]:
                i += 1
        return result
        
# @lc code=end

