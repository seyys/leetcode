/*
 * @lc app=leetcode id=5 lang=typescript
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
function longestPalindrome(s: string): string {
    let longestPalindrome = s[0] ?? '';

    const checkPalindrome = (leftCursor, rightCursor) => {
        for (let j = 0; j < s.length; j++) {
            leftCursor -= 1;
            rightCursor += 1;
            if (leftCursor < 0) break;
            if (rightCursor >= s.length) break;
            if (s[leftCursor] !== s[rightCursor]) break;
        }
        if (longestPalindrome.length < (rightCursor - leftCursor - 1)) {
            longestPalindrome = s.slice(leftCursor + 1, rightCursor);
        }
    }

    for (let i = 0; i < s.length - Math.ceil(longestPalindrome.length / 2); i++) {
        checkPalindrome(i, i);
        if (s[i] === s[i + 1]) checkPalindrome(i, i + 1);
    }

    return longestPalindrome;
};
// @lc code=end

