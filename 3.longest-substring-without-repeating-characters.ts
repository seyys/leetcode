/*
 * @lc app=leetcode id=3 lang=typescript
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
// @ts-ignore
function lengthOfLongestSubstring(s: string): number {
    const str = s.split('');
    const minLens: number[] = new Array(s.length).fill(0);
    var maxMinLen = 0;
    for (var i = s.length - 1; i >= 0; i--) {
        const char = str[i];
        const substr = str.slice(i + 1);
        const lengthBetweenRepeats = substr.findIndex(c => c === char);
        const minLen = lengthBetweenRepeats >= 0 ? lengthBetweenRepeats + 1 : substr.length + 1;
        const sublist = [minLen, ...minLens.slice(i + 1, i + minLen)];
        minLens[i] = (sublist.length > 0) ? Math.min(...sublist.map((len, j) => len + j)) : 0;
        if (minLens[i] > maxMinLen) maxMinLen = minLens[i];
    }
    return maxMinLen;
};
// @lc code=end

