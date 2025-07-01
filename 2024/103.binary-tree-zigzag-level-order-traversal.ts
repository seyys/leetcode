/*
 * @lc app=leetcode id=103 lang=typescript
 *
 * [103] Binary Tree Zigzag Level Order Traversal
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

function zigzagLevelOrder(root: TreeNode | null): number[][] {
  let queue: TreeNode[] = [root];
  let nextQueue: TreeNode[] = [];
  let reverse = false;
  const result: number[][] = [];
  let row: number[] = [];

  while (queue.length > 0) {
    queue.forEach((node) => {
      if (!node) {
        return;
      }
      row.push(node.val);
      nextQueue.push(node.left);
      nextQueue.push(node.right);
    });
    if (row.length === 0) {
      break;
    }
    result.push(reverse ? row.reverse() : row);
    queue = [...nextQueue];
    nextQueue = [];
    row = [];
    reverse = !reverse;
  }

  return result;
}
// @lc code=end
