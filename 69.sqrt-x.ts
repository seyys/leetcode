/*
 * @lc app=leetcode id=69 lang=typescript
 *
 * [69] Sqrt(x)
 */

// @lc code=start
function mySqrt(x: number): number {
    if (x === 0) return 0;
    let lowerBound = 1;
    let upperBound = x;
    while (true) {
        if (lowerBound + 1 >= upperBound) return lowerBound;
        const guess = Math.floor(lowerBound + (upperBound - lowerBound) / 2);
        const val = x / guess;
        if (guess > val) upperBound = guess;
        else lowerBound = guess;
    }
};
// @lc code=end