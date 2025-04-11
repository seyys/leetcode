#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_counter = defaultdict(int)
        s2_counter = defaultdict(int)

        for word in s1.split(' '):
            s1_counter[word] += 1
        for word in s2.split(' '):
            s2_counter[word] += 1

        s1_set = set()
        s2_set = set()
        for k, v in s1_counter.items():
            if v > 1 or k in s2_counter:
                continue
            s1_set.add(k)
        for k, v in s2_counter.items():
            if v > 1 or k in s1_counter:
                continue
            s2_set.add(k)
        
        return [x for x in s1_set.symmetric_difference(s2_set)]

# @lc code=end

