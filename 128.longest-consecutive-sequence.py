#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        max_len = 0
        for num in hashmap:
            if num - 1 in hashmap:
                continue
            current_len = 0
            while num in hashmap:
                num += 1
                current_len += 1
            max_len = max(max_len, current_len)
        return max_len

# @lc code=end

