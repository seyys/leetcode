#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        min_left = nums[left]
        pos_target = target < min_left

        while left <= right:
            mid = (left + right) // 2
            val = nums[mid]
            pos_num = val < min_left
            if val == target:
                return mid
            elif val > target:
                if pos_num != pos_target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if pos_num != pos_target:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
# @lc code=end

