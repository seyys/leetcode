/*
 * @lc app=leetcode id=95 lang=typescript
 *
 * [95] Unique Binary Search Trees II
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */
function generateTrees(n: number): Array<TreeNode | null> {
  const vals = new Array(n).fill(0).map((_, i) => i + 1);

  function dfs(left: number, right: number): Array<TreeNode | null> {
    if (left > right) {
      return [null];
    }
    if (left === right) {
      return [new TreeNode(vals[left])];
    }
    const result: Array<TreeNode | null> = [];
    for (let i = left; i <= right; i++) {
      const leftBranches = dfs(left, i - 1);
      const rightBranches = dfs(i + 1, right);
      for (const leftB of leftBranches) {
        for (const rightB of rightBranches) {
          result.push(new TreeNode(vals[i], leftB, rightB));
        }
      }
    }

    return result;
  }

  return dfs(0, vals.length - 1);
}
// @lc code=end
