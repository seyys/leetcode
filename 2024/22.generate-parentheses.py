#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # def generate(n, m, open_brackets, close_brackets):
        #     if m == 0: 
        #         return [')']
        #     if n == 0:
        #         return [')' * m]
        #     opening = [f'({x}' for x in generate(n - 1, m - 1, open_brackets + 1, close_brackets)]
        #     if close_brackets < open_brackets:
        #         closing = [f'){x}' for x in generate(n, m - 1, open_brackets, close_brackets + 1)]
        #         opening.extend(closing) if closing else opening
        #     return opening
        # return generate(n, 2*n, 0, 0)
        stack = []
        result = []

        def generate(opened, closed):
            if opened == closed == n:
                result.append("".join(stack))
                return
            
            if opened < n:
                stack.append('(')
                generate(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(')')
                generate(opened, closed + 1)
                stack.pop()

        generate(0,0)
        return result

# @lc code=end
