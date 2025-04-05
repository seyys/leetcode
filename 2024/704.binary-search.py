#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            curr = (high - low) // 2 + low
            if target > nums[curr]:
                low = curr + 1
            elif target < nums[curr]:
                high = curr - 1
            else:
                return curr
        return -1
# @lc code=end

