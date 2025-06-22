/*
 * @lc app=leetcode id=38 lang=typescript
 *
 * [38] Count and Say
 */

// @lc code=start
function countAndSay(n: number): string {
    let result = "1";
    for (let i = 1; i < n; i++) {
      let idx = 0;
      let new_result = ""
      while (idx < result.length) {
        const curr = result[idx];
        const curr_idx = idx;
        while (result[idx] === curr) {
          idx++;
        }
        new_result += `${idx - curr_idx}${curr}`
      }
      result = new_result;
    }

    return result;
};
// @lc code=end

