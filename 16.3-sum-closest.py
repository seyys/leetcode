#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest_val = 100000
        for i in range(len(nums) - 2):
            val = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                val_sum = val + nums[left] + nums[right]
                if abs(target - val_sum) < abs(target - closest_val):
                    closest_val = val_sum
                if val_sum == target:
                    return val_sum
                elif val_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_val
# @lc code=end

