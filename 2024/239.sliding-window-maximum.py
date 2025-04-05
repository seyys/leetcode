#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

from collections import deque

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_idx = deque()
        result = []
        for i in range(len(nums)):
            while len(max_idx) > 0 and max_idx[0] <= i - k:
                max_idx.popleft()
            while len(max_idx) > 0 and nums[i] >= nums[max_idx[-1]]:
                max_idx.pop()
            max_idx.append(i)
            if i - k + 1 < 0:
                continue
            result.append(nums[max_idx[0]])
        return result
# @lc code=end

