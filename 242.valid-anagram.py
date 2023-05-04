#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        for c in list(s):
            s_map[c] = 1 + s_map.get(c, 0)
        for c in list(t):
            if s_map.get(c, 0) == 0:
                return False
            s_map[c] -= 1
        return True
# @lc code=end

