#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        freq = [[] for x in range(len(nums) + 1)]
        for num, count in counter.items():
            freq[count].append(num)
        result = []
        for i in range(len(freq) - 1, -1, -1):
            result.extend(freq[i])
            if len(result) >= k:
                return result
# @lc code=end

