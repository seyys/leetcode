#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_map = {'{': '}', '[': ']', '(': ')'}
        for c in s:
            if len(stack) == 0 and c not in close_map:
                return False
            if c in close_map:
                stack.append(c)
            elif close_map[stack[-1]] != c:
                return False
            else:
                stack.pop()
        return len(stack) == 0
# @lc code=end

