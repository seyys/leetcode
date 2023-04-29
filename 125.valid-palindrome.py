#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alphanumeric(c):
            return (c <= "z" and c >= "a") or (c <= "Z" and c >= "A") or (c <= "9" and c >= "0")
        if len(s) <= 1:
            return True
        left = 0
        right = len(s) - 1
        while (left < right):
            while left < right and not is_alphanumeric(s[left]):
                left += 1
            while right > left and not is_alphanumeric(s[right]):
                right -= 1
            if (not left < right):
                break
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        
# @lc code=end