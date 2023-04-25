/*
 * @lc app=leetcode id=13 lang=typescript
 *
 * [13] Roman to Integer
 */

// @lc code=start
function romanToInt(s: string): number {
    const RomanNum: { [k in string]: number } = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    const romanStr = s.split('');
    return romanStr.reduce((partialSum, character, i) => {
        const currentNum = RomanNum[character];
        const nextNum = RomanNum[romanStr[i + 1]];
        if (nextNum === undefined) return partialSum + currentNum;
        if (nextNum > currentNum) return partialSum - currentNum;
        return partialSum + currentNum;
    }, 0);
};
// @lc code=end

