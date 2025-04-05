#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set_nums = set(nums)
        # done = set()
        # max_chain = 0
        # for num in nums:
        #     if num in done:
        #         continue
        #     current_chain = 1
        #     done.add(num)
        #     lower = num - 1
        #     while lower in set_nums:
        #         current_chain += 1
        #         done.add(lower)
        #         lower -= 1
        #     higher = num + 1
        #     while higher in set_nums:
        #         current_chain += 1
        #         done.add(higher)
        #         higher += 1
        #     max_chain = max(max_chain, current_chain)
        # return max_chain
        set_nums = set(nums)
        max_chain = 0
        for num in nums:
            if num - 1 in set_nums:
                continue
            current_chain = 1
            while num + 1 in set_nums:
                current_chain += 1
                num += 1
            max_chain = max(max_chain, current_chain)
        return max_chain

# @lc code=end

