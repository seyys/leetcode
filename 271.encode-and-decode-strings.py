#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#

# @lc code=start
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs: List[str]) -> str:
        output = strs[0]
        for i in range(1, len(strs)):
            output += f',/{strs[i].replace("/", "//")}/'
        return output

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, s) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            word = ''
            if s[i] == '/':
                i += 1
            while True:
                while s[i] != '/':
                    word += s[i]
                    i += 1
                if s[i+1] != '/':
                    output.append(word)
                    continue
                i += 1
        return output

# @lc code=end

