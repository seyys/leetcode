/*
 * @lc app=leetcode id=40 lang=typescript
 *
 * [40] Combination Sum II
 */

// @lc code=start
function combinationSum2(candidates: number[], target: number): number[][] {
  function calc(candidates: number[], target: number): number[][] {
    const result: number[][] = [];
    for (let i = 0; i < candidates.length; i++) {
      if (target - candidates[i] < 0) {
        continue;
      } else if (i > 0 && candidates[i] === candidates[i - 1]) {
        continue;
      } else if (target - candidates[i] === 0) {
        result.push([candidates[i]]);
      } else {
        result.push(
          ...calc(candidates.slice(i + 1), target - candidates[i]).map(
            (arr) => [...arr, candidates[i]],
          ),
        );
      }
    }

    return result;
  }

  candidates.sort();
  return calc(candidates, target);
}
// @lc code=end
