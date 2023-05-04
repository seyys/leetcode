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
        freq = [[] for i in range(len(nums) + 1)]
        for val, count in counter.items():
            freq[count].append(val)
        result = [] 
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                result.append(freq[i][j])
                if len(result) >= k:
                    return result
        return result
        
# @lc code=end

