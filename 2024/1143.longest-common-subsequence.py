#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0] * (len(text2) + 1) for _ in range(len(text1)+1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    max_length = 1 + memo[i+1][j+1]
                else:
                    max_length = max(memo[i][j+1], memo[i+1][j])
                memo[i][j] = max_length
        return max(max(memo))
# @lc code=end

