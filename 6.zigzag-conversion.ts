/*
 * @lc app=leetcode id=6 lang=typescript
 *
 * [6] Zigzag Conversion
 */

// @lc code=start
function convert(s: string, numRows: number): string {
    let result = '';
    const numEls = s.length;
    const increment = Math.max((numRows - 1) * 2, 1);
    for (let i = 0; i < numRows; i++) {
        const offset = (numRows - i - 1) * 2;
        for (let idx = i; idx < numEls; idx += increment) {
            result += s[idx];
            if (idx + offset >= numEls) break;
            if (offset === 0 || offset === ((numRows - 1) * 2)) continue;
            result += s[idx + offset];
        }
    }
    return result;
};
// @lc code=end
