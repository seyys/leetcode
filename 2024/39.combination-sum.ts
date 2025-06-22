/*
 * @lc app=leetcode id=39 lang=typescript
 *
 * [39] Combination Sum
 */

// @lc code=start
function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];
  candidates.forEach((candidate, i) => {
    if (target - candidate < 0) {
      return;
    } else if (target - candidate === 0) {
      result.push([candidate]);
    } else {
      result.push(
        ...combinationSum(candidates.slice(i), target - candidate)
          .map((arr) => [...arr, candidate]),
      );
    }
  });

  return result;
}
// @lc code=end
