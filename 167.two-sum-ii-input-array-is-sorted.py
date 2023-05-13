#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            val = numbers[left] + numbers[right]
            if val == target:
                return [left + 1, right + 1]
            elif val < target:
                left += 1
            else:
                right -= 1                    
# @lc code=end

