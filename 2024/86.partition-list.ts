/*
 * @lc app=leetcode id=86 lang=typescript
 *
 * [86] Partition List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function partition(head: ListNode | null, x: number): ListNode | null {
  const pLower = new ListNode();
  const pUpper = new ListNode();
  let nodeLower = pLower;
  let nodeUpper = pUpper;
  let node = head;
  while (node) {
    if (node.val < x) {
      nodeLower.next = node;
      nodeLower = nodeLower.next;
    } else {
      nodeUpper.next = node;
      nodeUpper = nodeUpper.next;
    }
    node = node.next;
  }
  nodeLower.next = pUpper.next;
  nodeUpper.next = null;

  return pLower.next;
}
// @lc code=end
