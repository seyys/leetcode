/*
 * @lc app=leetcode id=70 lang=typescript
 *
 * [70] Climbing Stairs
 */

// @lc code=start
function factorial(x: number): number {
    if (x === 0) return 1;
    return x * factorial(x - 1);
}

function permutation(total: number, a: number, b: number): number {
    return factorial(total) / (factorial(a) * factorial(b));
}

function climbStairs(n: number): number {
    let count = 0;
    let num1steps = n;
    let num2steps = 0;
    for (let numSteps = n; numSteps >= (n / 2); numSteps--) {
        count += permutation(numSteps, num1steps, num2steps);
        num1steps -= 2;
        num2steps++;
    }
    return count;
};
// @lc code=end