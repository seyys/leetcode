#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        num2letter = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        def backtrack(i: int, substr: str):
            if len(substr) == len(digits):
                result.append(substr)
                return
            for letter in num2letter[digits[i]]:
                backtrack(i + 1, substr + letter)
        result = []
        backtrack(0, '')
        return result
# @lc code=end

