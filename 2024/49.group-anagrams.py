#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        hashmap = {}
        for s in strs:
            freq = self.get_letter_frequency(s)
            out[freq].append(s)
        return out.values()

    def get_letter_frequency(self, s: str):
        freq = 26 * [0]
        for char in s:
            freq[ord(char) - ord('a')] += 1
        return tuple(freq)

# @lc code=end

