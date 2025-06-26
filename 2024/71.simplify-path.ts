/*
 * @lc app=leetcode id=71 lang=typescript
 *
 * [71] Simplify Path
 */

// @lc code=start
function simplifyPath(path: string): string {
  const p = path.split('/');
  const result: string[] = [];

  for (let stub of p) {
    if (stub.length === 0 || stub === '.') {
      continue;
    } else if (stub === '..') {
      result.pop();
    } else {
      result.push(stub);
    }
  }

  return `/${result.join('/')}`;
}
// @lc code=end
