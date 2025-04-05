#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        p1 = len(nums1) // 2
        p2 = total_len // 2 - p1
        while True:
            if nums1[p1] 

# @lc code=end


[] [1,2,3] ans = 2
