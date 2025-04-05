#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            guess = (right - left) // 2 + left
            print(guess, left, right, nums[guess], nums[left], nums[right], nums[guess] > target)
            if nums[guess] == target:
                return guess
            elif nums[guess] < target:
                if nums[right] > nums[left]:
                    left = guess + 1
                elif nums[guess] > nums[left]:
                    right = guess - 1
                else:
                    left = guess + 1
            else:
                if nums[right] > nums[left]:
                    right = guess - 1
                else:
                    left = guess + 1
        return -1
# @lc code=end

