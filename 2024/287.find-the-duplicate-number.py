#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        minN = 1
        maxN = len(nums) - 1
        minP = minN
        maxP = maxN
        minS = minN
        maxS = maxN
        p = 1
        s = 0
        for i, num in enumerate(nums):
            p *= num
            s += num
            if p < minP or p > maxP or s < minS or s > maxS:
                return num
            minN += 1
            maxN -= 1
            minP *= minN
            maxP *= maxN
            minS += minN
            maxS += maxN
        x = 0
        for i in range(len(nums)):
            x ^= i

        for num in nums:
            x ^= num

        return x
        
# @lc code=end

