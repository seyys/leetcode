#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right  = 0, len(nums) - 1
        current_min = min(nums[left], nums[right])
        
        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid, current_min)
            if nums[mid] < current_min:
                current_min = nums[mid]
                right = mid - 1
            else:
                left = mid + 1

        return current_min

# @lc code=end

