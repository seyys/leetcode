#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_primitives = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4:'IV', 1: 'I'
        }
        result = ""
        for denominator in roman_primitives:
            remainder = num // denominator
            num -= remainder * denominator
            result += roman_primitives[denominator] * remainder
        return result
        
# @lc code=end

