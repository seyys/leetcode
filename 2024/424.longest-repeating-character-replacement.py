#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

from collections import Counter

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        count = Counter()
        l = 0
        for r in range(len(s)):
            count.update(s[r])
            while r - l + 1 > count.most_common(1)[0][1] + k:
                count.subtract(s[l])
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len
# @lc code=end

