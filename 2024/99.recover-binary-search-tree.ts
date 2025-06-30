/*
 * @lc app=leetcode id=99 lang=typescript
 *
 * [99] Recover Binary Search Tree
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

/**
 Do not return anything, modify root in-place instead.
 */
function recoverTree(root: TreeNode | null): void {
  function dfs(root: TreeNode | null) {
    if (!root) {
      return;
    }
    dfs(root.left);
    inorder.push(root);
    dfs(root.right);
  }

  const inorder: TreeNode[] = [];
  dfs(root);
  const sorted = inorder.map((node) => node.val).sort((a, b) => a - b);
  for (let i = 0; i < inorder.length; i++) {
    inorder[i].val = sorted[i];
  }
}
// @lc code=end
