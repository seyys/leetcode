/*
 * @lc app=leetcode id=82 lang=typescript
 *
 * [82] Remove Duplicates from Sorted List II
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

function deleteDuplicates(head: ListNode | null): ListNode | null {
  let dummy = new ListNode();
  dummy.next = head;
  let slow = dummy;
  let fast = head;
  while (fast) {
    while (fast && fast.val === slow.next.val) {
      fast = fast.next;
    }
    if (slow.next.next !== fast) {
      slow.next = fast;
    } else {
      slow = slow.next;
    }
    fast = fast ? fast.next : fast;
  }

  return dummy.next;
}
// @lc code=end
