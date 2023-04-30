#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        # Populate hashtable
        hashtable = {}
        for i, num in enumerate(nums):
            if num not in hashtable:
                hashtable[num] = i
                continue
            hashtable[num] = max(i, hashtable[num])
        result = []
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                k = j + 1
                while k < len(nums) - 1:
                    remainder = target - (nums[i] + nums[j] + nums[k])
                    if remainder in hashtable:
                        if hashtable[remainder] > k:
                            result.append([nums[i], nums[j], nums[k], remainder])
                    k += 1
                    while k < len(nums) - 1 and nums[k] == nums[k - 1]:
                        k += 1    
                j += 1
                while j < len(nums) - 2 and nums[j] == nums[j - 1]:
                    j += 1
            i += 1
            while i < len(nums) - 3 and nums[i] == nums[i - 1]:
                i += 1
        return result
        
# @lc code=end

