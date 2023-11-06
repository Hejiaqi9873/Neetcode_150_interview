# 146. LRU Cache

class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None
class LRUCache:

    # O(1) average time
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {} # key -> Node
        # left: LRU, right: most recent used
        self.left, self.right  = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from the linked list
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    # insert node into the right position
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev
        pass

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # Todi: update most recent
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        self.hashmap[key] = Node(key, value)
        self.insert(self.hashmap[key])

        if len(self.hashmap) > self.cap:
            # remove the least used item
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]




    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     self.hashmap = {}
    #     self.stack = []
    #
    # def get(self, key: int) -> int:
    #     if key in self.hashmap:
    #
    #         value = self.hashmap[key][1]
    #         pop_index = self.stack.index([key, value])
    #         self.stack.pop(pop_index)
    #         self.stack.append([key, value])
    #
    #         return value
    #     else:
    #         return -1
    #
    # def put(self, key: int, value: int) -> None:
    #     if key in self.hashmap:
    #         value_cur = self.hashmap[key]
    #         self.hashmap.pop(key)
    #         index = self.stack.index(value_cur)
    #         self.stack.pop(index)
    #         self.stack.append([key, value])
    #         self.hashmap[key] = [key, value]
    #     else:
    #         if len(self.stack) < self.capacity:
    #             self.stack.append([key, value])
    #             self.hashmap[key] = [key, value]
    #         else:
    #             remove_key = self.stack[0][0]
    #             self.stack.pop(0)
    #             self.hashmap.pop(remove_key)
    #             self.stack.append([key, value])
    #             self.hashmap[key] = [key, value]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)