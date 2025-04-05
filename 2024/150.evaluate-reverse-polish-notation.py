#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

import math

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if t == '+':
                    stack.append(val1 + val2)
                elif t == '-':
                    stack.append(val1 - val2)
                elif t == '*':
                    stack.append(val1 * val2)
                elif t == '/':
                    stack.append(math.trunc(val1 / val2))
        return stack[0]
# @lc code=end

