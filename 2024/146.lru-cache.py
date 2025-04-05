#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from collections import defaultdict

class ListNode:
    def __init__(self, x):
        self.key = x
        self.next = None
        self.prev = None

class Node:
    def __init__(self,):
        self.val = None
        self.node = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_capacity = 0
        self.mru_head = ListNode(0)
        self.lru_head = ListNode(0)
        self.mru_head.prev = self.lru_head
        self.lru_head.next = self.mru_head
        self.hashmap = {}

    def get(self, key: int) -> int:
        # get val of key
        if key not in self.hashmap:
            return -1

        # if key exists, make mru
        self.make_mru(self.hashmap[key].node)
        # else return -1
        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        # if key exists, Update val of key 
        if key in self.hashmap:
            node = self.hashmap[key].node
        # else insert
        else: 
            node = ListNode(key)
            self.hashmap[key] = Node()
            self.hashmap[key].node = node
            self.current_capacity += 1
        self.hashmap[key].val = value

        # Make key mru
        self.make_mru(node)

        # If new capacity > capacity, evict lru
        if self.current_capacity > self.capacity:
            lru_node = self.lru_head.next
            self.lru_head.next = lru_node.next
            lru_node.next.prev = self.lru_head
            self.hashmap.pop(lru_node.key)
            self.current_capacity -= 1
    
    def make_mru(self, node: ListNode):
        if node.prev is not None and node.next is not None:
            node.prev.next = node.next
            node.next.prev = node.prev

        mru_node = self.mru_head.prev
        node.next = self.mru_head
        node.prev = mru_node
        mru_node.next = node
        self.mru_head.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

