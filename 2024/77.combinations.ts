/*
 * @lc app=leetcode id=77 lang=typescript
 *
 * [77] Combinations
 */

// @lc code=start
function combine(n: number, k: number): number[][] {
  const result: number[][] = [];
  function backtrack(start: number, combinations: number[]) {
    if (combinations.length === k) {
      result.push([...combinations]);
    }
    for (let i = start; i <= n; i++) {
      combinations.push(i);
      backtrack(i + 1, combinations);
      combinations.pop();
    }
  }

  backtrack(1, []);
  return result;
}
// @lc code=end
