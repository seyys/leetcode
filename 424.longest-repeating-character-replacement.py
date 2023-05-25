#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = defaultdict(int)
        longest_substring = 0
        left = 0
        for right in range(len(s)):
            count_map[s[right]] += 1
            while (right - left + 1) - max(count_map.values()) > k:
                count_map[s[left]] -= 1
                left += 1
            longest_substring = max(longest_substring, right - left + 1)
        return longest_substring

# @lc code=end

