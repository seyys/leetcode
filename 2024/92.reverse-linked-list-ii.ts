/*
 * @lc app=leetcode id=92 lang=typescript
 *
 * [92] Reverse Linked List II
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

function reverseBetween(
  head: ListNode | null,
  left: number,
  right: number,
): ListNode | null {
  const dummy = new ListNode();
  dummy.next = head;

  let i = 0;
  let node = dummy;
  for (; i < left - 1; i++) {
    node = node.next;
  }
  const leftPrevNode = node;
  node = node.next;
  let nextNode = node.next;
  for (; i < right - 1; i++) {
    const nextNextNode = nextNode.next;
    nextNode.next = node;
    node = nextNode;
    nextNode = nextNextNode;
  }
  leftPrevNode.next.next = nextNode;
  leftPrevNode.next = node;

  return dummy.next;
}
// @lc code=end
