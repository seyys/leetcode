#
# @lc app=leetcode id=2187 lang=python3
#
# [2187] Minimum Time to Complete Trips
#

# @lc code=start
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def num_trips(time, guess: int):
            return sum([guess // t for t in time])

        min_time = min(time)
        l = min_time
        r = min_time * totalTrips
        while l < r:
            guess = (r - l) // 2 + l
            if num_trips(time, guess) >= totalTrips:
                r = guess
            else: 
                l = guess + 1

        return l

# @lc code=end

