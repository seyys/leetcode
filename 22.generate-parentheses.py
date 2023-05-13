#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def populate_set(string, brackets_open, brackets_close):
            if brackets_open < 0 or brackets_close < 0 or brackets_open > brackets_close:
                return
            if brackets_open + brackets_close > 0:
                populate_set(string + '(', brackets_open - 1, brackets_close)
                populate_set(string + ')', brackets_open, brackets_close - 1)
            else:
                result.append(string)

        populate_set('', n, n)
        return result

# @lc code=end

