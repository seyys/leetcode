#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        def checkPalindrome(left, right):
            if s[left] != s[right]:
                return
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                self.result += 1

        self.result = 0
        for i in range(len(s)):
            checkPalindrome(i, i)
            if i + 1 < len(s):
                checkPalindrome(i, i+1)
        return self.result
# @lc code=end

