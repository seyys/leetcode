/*
 * @lc app=leetcode id=9 lang=typescript
 *
 * [9] Palindrome Number
 */

// @lc code=start
function isPalindrome(x: number): boolean {
    if (x < 0) return false;
    const num = x.toString();
    var i = 0;
    var j = num.length - 1;
    while (i < j) {
        if (num[i++] !== num[j--]) return false;
    }
    return true;
};
// @lc code=end

