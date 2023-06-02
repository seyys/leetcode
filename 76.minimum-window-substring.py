#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = defaultdict(int)
        for c in t:
            counter_t[c] += 1
        need = len(counter_t.items())
        
        right = 0
        counter_s = defaultdict(int)
        result = ""
        have = 0
        for left in range(len(s)):
            while right < len(s) and have < need:
                counter_s[s[right]] += 1
                if counter_t[s[right]] > 0 and counter_t[s[right]] == counter_s[s[right]]:
                    have += 1
                right += 1
            if have == need:
                if result == "" or len(result) > right - left:
                    result = s[left:right]
            counter_s[s[left]] -= 1
            if counter_t[s[left]] > 0 and counter_t[s[left]] > counter_s[s[left]]:
                have -= 1
            left += 1
        return result
        
# @lc code=end

