/*
 * @lc app=leetcode id=106 lang=typescript
 *
 * [106] Construct Binary Tree from Inorder and Postorder Traversal
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

function buildTree(inorder: number[], postorder: number[]): TreeNode | null {
  function dfs(inorderMin: number, inorderMax: number) {
    if (postorderIdx < 0 || inorderMin > inorderMax) {
      return null;
    }
    const val = postorder[postorderIdx--];
    const node = new TreeNode(val);
    node.right = dfs(inorderMap[val] + 1, inorderMax);
    node.left = dfs(inorderMin, inorderMap[val] - 1);
    return node;
  }

  const inorderMap: { [key in number]: number } = {};
  inorder.forEach((val, i) => (inorderMap[val] = i));
  let postorderIdx = postorder.length - 1;

  return dfs(0, inorder.length - 1);
}
// @lc code=end
