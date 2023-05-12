#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip('-').isnumeric():
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                match token:
                    case '-':
                        stack.append(a-b)
                    case '+':
                        stack.append(a+b)
                    case '*':
                        stack.append(a*b)
                    case '/':
                        stack.append(int(a/b))
        return stack[0]
# @lc code=end

