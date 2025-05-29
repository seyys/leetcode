/*
 * @lc app=leetcode id=2 lang=typescript
 *
 * [2] Add Two Numbers
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

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  let node1 = l1;
  let node2 = l2;
  const dummy = new ListNode();
  let root = dummy;
  let carry = 0;
  
  while (node1 !== null || node2 !== null || carry > 0) {
    const val = ((node1?.val ?? 0) + (node2?.val ?? 0) + carry) % 10
    carry = Math.floor(((node1?.val ?? 0) + (node2?.val ?? 0) + carry) / 10)
    const node = new ListNode(val)
    root.next = node;

    root = root.next;
    node1 = node1 ? node1.next : node1;
    node2 = node2 ? node2.next : node2;
  }

  return dummy.next;
};
// @lc code=end

