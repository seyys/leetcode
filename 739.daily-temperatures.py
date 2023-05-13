#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        min_temp_log = []
        for i, temp in enumerate(temperatures):
            while len(min_temp_log) > 0 and min_temp_log[-1][1] < temp:
                j, _ = min_temp_log.pop()
                result[j] = i - j
            min_temp_log.append((i, temp))
        return result

# @lc code=end

