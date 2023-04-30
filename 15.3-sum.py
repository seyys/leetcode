#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums = sorted(nums)
        hashmap = {}
        result = set()
        # O(n)
        for i, num in enumerate(nums):
            if num in hashmap:
                hashmap[num].append(i)
            else:
                hashmap[num] = [i]
        # O(n^2)
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1:
                remainder = target - (nums[i] + nums[j])
                if remainder in hashmap:
                    if max(hashmap[remainder]) > max(i,j):
                        result.add(tuple(sorted([nums[i], nums[j], remainder])))
                        current_val = nums[i]
                        while i < len(nums) - 2 and nums[i + 1] == current_val:
                            i += 1
                        j = max(i, j)
                j += 1
            i += 1
        return result
# @lc code=end

