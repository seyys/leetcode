#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []

        for num in nums:
            heapq.heappush(result, num)
            if len(result) > k:
                heapq.heappop(result)
        
        return result[0]
        
# @lc code=end

