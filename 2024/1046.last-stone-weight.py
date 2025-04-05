#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
            new_stone = abs(stone1 - stone2)
            if new_stone != 0:
                heapq.heappush(stones, -new_stone)

        if len(stones) == 0:
            return 0
        return -heapq.heappop(stones)

# @lc code=end

