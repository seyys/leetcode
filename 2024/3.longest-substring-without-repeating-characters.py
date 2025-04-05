#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        seen = set()
        max_len = 0
        p1 = 0
        p2 = 0
        while p2 < len(s):
            if s[p2] in seen:
                while p1 < p2 and s[p1] != s[p2]:
                    seen.discard(s[p1])
                    p1 += 1
                p1 += 1
            seen.add(s[p2])
            max_len = max(p2 - p1 + 1, max_len)
            p2 += 1
        return max_len

# @lc code=end

