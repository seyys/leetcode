/*
 * @lc app=leetcode id=97 lang=typescript
 *
 * [97] Interleaving String
 */

// @lc code=start
function isInterleave(s1: string, s2: string, s3: string): boolean {
  const result: boolean[] = new Array(s2.length + 1).fill(false);

  if (s1.length + s2.length !== s3.length) {
    return false;
  }

  for (let p1 = s1.length; p1 >= 0; p1--) {
    for (let p2 = s2.length; p2 >= 0; p2--) {
      const idx = p1 + p2;
      if (
        (p1 === s1.length && p2 === s2.length) ||
        (s3[idx] === s1[p1] && result[p2]) ||
        (s3[idx] === s2[p2] && result[p2 + 1])
      ) {
        result[p2] = true;
        continue;
      }
      result[p2] = false;
    }
  }

  return result[0];
}
// @lc code=end
