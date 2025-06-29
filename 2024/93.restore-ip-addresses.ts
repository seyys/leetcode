/*
 * @lc app=leetcode id=93 lang=typescript
 *
 * [93] Restore IP Addresses
 */

// @lc code=start
function restoreIpAddresses(s: string): string[] {
  const result: string[] = [];
  const ip: string[] = [];

  function backtrack(i: number) {
    const lastOctet = ip.at(-1);
    // Can't have more than 4 octets
    if (ip.length > 4) {
      return;
    }
    if (!!lastOctet) {
      // Can't start with 0 if multiple digits
      if (lastOctet.length > 1 && lastOctet[0] === '0') {
        return;
      }
      // Can't be more than 255
      if (Number(lastOctet) > 255) {
        return;
      }
    }
    if (i >= s.length && ip.length === 4) {
      result.push(ip.join('.'));
      return;
    }

    for (let j = 1; j <= 3 && i + j <= s.length; j++) {
      ip.push(s.slice(i, i + j));
      backtrack(i + j);
      ip.pop();
    }
  }

  backtrack(0);
  return result;
}
// @lc code=end
