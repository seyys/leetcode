#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        nums = [float('-inf')] + nums
        for i in range(1, len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            if changed:
                return False
            if nums[i+1] < nums[i-1]:
                nums[i+1] = nums[i]
            else:
                nums[i] = nums[i+1]
            changed = True
        return True
# @lc code=end

