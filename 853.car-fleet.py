#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        params = list(zip(position, speed)) # [(pos1, speed1),...]
        params.sort(key=lambda x: -x[0])
        fleets = []
        for p, v in params:
            t = (target - p) / v
            if len(fleets) > 0 and t <= fleets[-1]:
                continue
            fleets.append(t)
        return len(fleets)

# @lc code=end

