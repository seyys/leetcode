#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calc_distance(x, y):
            return math.sqrt(x**2 + y**2)

        distances = []
        for p in points:
            heapq.heappush(distances, (-calc_distance(p[0], p[1]), p))
            if len(distances) > k:
                heapq.heappop(distances)

        return [point for [_, point] in distances]
# @lc code=end

