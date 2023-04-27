/*
 * @lc app=leetcode id=67 lang=typescript
 *
 * [67] Add Binary
 */

// @lc code=start
function addBinary(a: string, b: string): string {
    const maxLen = Math.max(a.length, b.length);
    const aPad = [...new Array(maxLen - a.length).fill(0), ...(a.split('').map(val => val === '0' ? 0 : 1))];
    const bPad = [...new Array(maxLen - b.length).fill(0), ...(b.split('').map(val => val === '0' ? 0 : 1))];
    let resultRaw = new Array(maxLen - 1).fill(0);
    let carry = 0;
    for (let i = maxLen - 1; i >= 0; i--) {
        const val = aPad[i] + bPad[i] + carry;
        carry = Math.floor(val / 2);
        resultRaw[i] = val % 2;
    }
    if (carry > 0) resultRaw = [carry, ...resultRaw];
    let result = resultRaw.join('').toString();
    return result;
};
// @lc code=end

