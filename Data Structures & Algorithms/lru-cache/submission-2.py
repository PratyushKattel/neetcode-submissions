class ListNode:
    def __init__(self,key,val,left = None,right =None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.lru,self.mru = ListNode(0,0) , ListNode(0,0)
        self.lru.right , self.mru.left = self.mru , self.lru

    def insert (self, Node):
        Node.left = self.mru.left
        Node.right = self.mru
        self.mru.left.right = Node
        self.mru.left = Node

    def remove(self,Node):
        prev_node = Node.left
        next_node = Node.right
        prev_node.right = next_node
        next_node.left = prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            Node = self.cache[key]
            self.remove(Node)
            self.insert(Node)
            return Node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            Node = self.cache[key]
            Node.val = value
            self.remove(Node)
            self.insert(Node)
            return 

        new_node = ListNode(key,value)
        if len(self.cache) < self.capacity :
            self.cache[key] = new_node
            self.insert(new_node)
        else:
            del self.cache[self.lru.right.key]
            self.remove(self.lru.right)
            self.cache[key] = new_node
            self.insert(new_node)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)