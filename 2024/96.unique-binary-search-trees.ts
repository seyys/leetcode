/*
 * @lc app=leetcode id=96 lang=typescript
 *
 * [96] Unique Binary Search Trees
 */

// @lc code=start
function numTrees(n: number): number {
  const results = [1];

  for (let i = 0; i < n; i++) {
    let result = 0;
    for (let j = 0; j <= i; j++) {
      result += results[j] * results[i - j];
    }
    results.push(result);
  }

  return results[n];
}
// @lc code=end
