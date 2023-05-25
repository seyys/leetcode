#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = [0] * 26
        seen = [0] * 26

        if len(s2) < len(s1):
            return False

        for c in s1:
            s1count[ord(c) - ord('a')] += 1
        for i in range(len(s1)):
            seen[ord(s2[i]) - ord('a')] += 1

        is_identical = sum([x != y for x, y in zip(s1count, seen)]) == 0
        if is_identical:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            seen[ord(s2[left]) - ord('a')] -= 1
            seen[ord(s2[right]) - ord('a')] += 1
            is_identical = sum([x != y for x, y in zip(s1count, seen)]) == 0
            if is_identical:
                return True
            left += 1
        return False

# @lc code=end

