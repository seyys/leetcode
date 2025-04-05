#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        num_fleets = 0
        last_time = 0
        d = sorted([(x, v) for x, v in zip(position, speed)], key=lambda y: -y[0])
        for i in range(len(d)):
            if (target - d[i][0]) / d[i][1] > last_time:
                num_fleets += 1
                last_time = (target - d[i][0]) / d[i][1]
        return num_fleets

# @lc code=end

