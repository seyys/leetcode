/*
 * @lc app=leetcode id=9 lang=typescript
 *
 * [9] Palindrome Number
 */

// @lc code=start
function isPalindrome(x: number): boolean {
    if (x < 0) return false;
    const num = x.toString();
    for (var i = 0; i < num.length / 2; i++) {
        if (num[i] !== num[num.length - 1 - i]) return false;
    }
    return true;
};
// @lc code=end

