#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

from collections import Counter

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        left = 0
        right = 0
        result = ''
        while right < len(s):
            if s[right] in count:
                count[s[right]] -= 1
            right += 1
            while left < right and all(x <= 0 for x in count.values()):
                if result == '' or len(result) > right - left:
                    result = s[left:right]
                if s[left] in count:
                    count[s[left]] += 1
                left += 1
        return result

# @lc code=end

