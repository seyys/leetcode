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
        combinations = [num2letter[d] for d in digits]
        prod = lambda combos: reduce(operator.mul, [len(combo) for combo in combos], 1)
        result = [""] * prod(combinations)
        for i, combo in enumerate(combinations):
            period = prod(combinations[i+1:])
            j = 0
            letter_idx = 0
            while j < len(result):
                for _ in range(period):
                    result[j] += combo[letter_idx]
                    j += 1
                letter_idx += 1
                if letter_idx >= len(combo):
                    letter_idx = 0
        return result
# @lc code=end

