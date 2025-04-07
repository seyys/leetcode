#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkPalindrome(left, right):
            if s[left] != s[right]:
                return
            while left > 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            if right - left + 1 > len(self.result):
                self.result = s[left:right+1]

        self.result = ''
        for i in range(len(s)):
            checkPalindrome(i, i)
            if i + 1 < len(s):
                checkPalindrome(i, i+1)

        return self.result
# @lc code=end

