#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_idx = [0]
        result = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while len(stack_idx) > 0 and temperatures[i] > temperatures[stack_idx[-1]]:
                date = stack_idx.pop()
                result[date] = i - date
            stack_idx.append(i)
        return result
# @lc code=end

