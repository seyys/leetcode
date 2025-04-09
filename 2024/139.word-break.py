#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @functools.cache
        def dfs(s):
            if len(s) == 0:
                return True
            for word in wordDict:
                if s[:len(word)] != word:
                    continue
                if dfs(s[len(word):]):
                    return True
            return False

        return dfs(s)

# @lc code=end

