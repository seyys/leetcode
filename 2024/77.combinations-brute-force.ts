/*
 * @lc app=leetcode id=77 lang=typescript
 *
 * [77] Combinations
 */

// @lc code=start
function combine(n: number, k: number): number[][] {
  function dfs(val: number, n: number, k: number): number[][] {
    // Impossible to get more combos
    if (n - val + 1 < k) {
      return [];
    }
    if (val > n) {
      return [];
    }
    let take: number[][] = [];
    let skip: number[][] = [];
    if (k === 1) {
      take = [[val]];
      skip = dfs(val + 1, n, k);
    } else {
      take = dfs(val + 1, n, k - 1).map((arr) => [val, ...arr]);
      skip = dfs(val + 1, n, k);
    }
    return [...take, ...skip];
  }

  return dfs(1, n, k);
}
// @lc code=end
