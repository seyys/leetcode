#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i >= len(s):
            return 0
        isNegative = False
        if s[i] == '-':
            i += 1
            isNegative = True
        elif s[i] == '+':
            i += 1
        digits = []
        while i < len(s) and s[i] >= '0' and s[i] <= '9':
            digits.append(int(s[i]))
            i += 1
        result = 0
        exponent = 1
        for i in range(len(digits) - 1, -1, -1):
            result += exponent * digits[i]
            exponent *= 10
        if isNegative:
            result = -result
        return max(min(result, 2**31 - 1), -2**31)
# @lc code=end

