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

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const head = new ListNode();
    var currentNode = head;
    var currentNodel1 = l1;
    var currentNodel2 = l2;
    var carry = 0;

    while (true) {
        const digit1 = currentNodel1?.val || 0;
        const digit2 = currentNodel2?.val || 0;
        currentNode.val = (digit1 + digit2 + carry) % 10;
        carry = Math.floor((digit1 + digit2 + carry) / 10);
        if (carry === 0 && (!currentNodel1 || !currentNodel1?.next) && (!currentNodel2 || !currentNodel2?.next)) break;
        currentNode.next = new ListNode();
        currentNode = currentNode.next;
        currentNodel1 = currentNodel1 ? currentNodel1.next : null;
        currentNodel2 = currentNodel2 ? currentNodel2.next : null;
    }

    return head;
};
// @lc code=end

