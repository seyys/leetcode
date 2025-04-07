#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    @functools.cache
    def numDecodings(self, s: str, tenSomething = False, twentySomething = False) -> int:
        if len(s) == 0:
            return 0 if tenSomething or twentySomething else 1
        nums = 0
        firstNum = int(s[0])
        if twentySomething and firstNum > 6:
            return 0
        if tenSomething or twentySomething:
            return self.numDecodings(s[1:])
        if firstNum == 0:
            return 0
        if firstNum == 1:
            return self.numDecodings(s[1:]) + self.numDecodings(s[1:], tenSomething=True)
        if firstNum == 2:
            return self.numDecodings(s[1:]) + self.numDecodings(s[1:], twentySomething=True)
        return self.numDecodings(s[1:])
# @lc code=end

