#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        targets = set(s1)
        init_count = self.populate_count(s1)
        count = init_count[:]
        total = len(s1)
        l = 0
        r = 0
        for r in range(len(s2)):
            if s2[r] in targets:
                count[ord(s2[r]) - ord('a')] -= 1
                total -= 1
                while count[ord(s2[r]) - ord('a')] < 0:
                    if s2[l] in targets:
                        count[ord(s2[l]) - ord('a')] += 1
                        total += 1
                    l += 1
            else:
                l = r
                count = init_count[:]
                total = len(s1)
            if total == 0:
                return True
        return False
    
    def populate_count(self, s):
        count = 26 * [0]
        for char in s:
            count[ord(char) - ord('a')] += 1
        return count

# @lc code=end

