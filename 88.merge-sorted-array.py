#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx1 = m - 1
        idx2 = n - 1
        for i in range(m + n - 1, -1, -1):
            if (idx2 < 0 or nums1[idx1] >= nums2[idx2]) and idx1 >= 0:
                nums1[i] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[i] = nums2[idx2]
                idx2 -= 1

# @lc code=end

# 4 0 0 0 0 0
# 1 2 3 5 6

# i1 i2 n1 n2
# 0  0  4  1
