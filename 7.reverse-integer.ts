/*
 * @lc app=leetcode id=7 lang=typescript
 *
 * [7] Reverse Integer
 */

// @lc code=start
function reverse(x: number): number {
    const str = x.toString().split('');
    const isNegative = str[0] === '-';
    const absStrReversed = isNegative ? str.slice(1).reverse() : str.reverse();
    const maxInt = (isNegative ? 2**31 - 1 : 2**31).toString();
    const absStrReversedZeroPadded = [...(new Array(maxInt.length - absStrReversed.length).fill('0')), ...absStrReversed];
    for (let i = 0; i < maxInt.length; i++) {
        if (absStrReversedZeroPadded[i] > maxInt[i]) return 0;
        else if (absStrReversedZeroPadded[i] < maxInt[i]) break;
    }
    return (isNegative ? -1 : 1) * Number(absStrReversed.join(''));
};
// @lc code=end

