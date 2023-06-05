#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:
    class Node:
        def __init__(self, key, value, prev_node = None, next_node = None):
            self.key = key
            self.val = value
            self.next = next_node
            self.prev = prev_node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mru = self.Node(0,0)
        self.lru = self.Node(0,0)
        self.mru.next = self.lru
        self.lru.prev = self.mru
        self.node = {}
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.node:
            return -1
        node = self.node[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.Node(key, value)
        if key in self.node:
            self.remove(self.node[key])
        self.insert(node)
        if self.size > self.capacity:
            self.remove()

    def insert(self, node):
        if node.key not in self.node:
            self.size += 1
        nxt = self.mru.next
        node.next = nxt
        nxt.prev = node
        node.prev = self.mru
        self.mru.next = node
        self.node[node.key] = node

    def remove(self, node = None):
        if not node:
            node = self.lru.prev
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        del self.node[node.key]
        self.size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

