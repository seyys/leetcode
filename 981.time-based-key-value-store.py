#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.data[key]) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            ts, val = self.data[key][mid]
            if ts == timestamp:
                return val
            elif ts <= timestamp:
                result = val
                left = mid + 1
            else:
                right = mid - 1
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

