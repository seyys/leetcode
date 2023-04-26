/*
 * @lc app=leetcode id=20 lang=typescript
 *
 * [20] Valid Parentheses
 */

// @lc code=start
function isValid(s: string): boolean {
    const stack: string[] = [];
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        switch (c) {
            case '(':
            case '[':
            case '{':
                stack.push(c);
                break;
            case ')':
                if (stack.pop() !== '(') return false;
                break;
            case ']':
                if (stack.pop() !== '[') return false;
                break;
            case '}':
                if (stack.pop() !== '{') return false;
                break;
        }
    }
    return stack.length === 0;
};
// @lc code=end

