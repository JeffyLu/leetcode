class Node:

    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        left = self.left.val if self.left is not None else "?"
        right = self.right.val if self.right is not None else "?"
        return '{}-{}-{}'.format(left, self.val, right)


class LRUCache:

    def __init__(self, capacity):
        self.cache = {}
        self.cap = capacity
        self.size = 0
        self.head = None
        self.tail = None

    def get(self, key):
        node = self.cache.get(key)
        if node is None:
            return -1
        self._move_to_head(node)
        return node.val

    def put(self, key, value):
        node = self.cache.get(key)
        if node is None:
            node = Node(value, key)
            self.cache[key] = node
            self.size += 1
        else:
            node.val = value
        self._move_to_head(node)
        self._del_tail()

    def _move_to_head(self, node):
        # 空链表
        if self.head is None:
            self.head = node
            self.tail = node
            return
        # node是头节点
        elif self.head == node:
            return
        # node是新节点
        if node.right is None and node.left is None:
            node.right = self.head
            self.head.left = node
            self.head = node
            return
        node.left.right = node.right
        # node是中间节点
        if node.right is not None:
            node.right.left = node.left
        # node是尾节点
        else:
            self.tail = node.left
        node.right = self.head
        self.head.left = node
        node.left = None
        self.head = node

    def _del_tail(self):
        while self.size > self.cap:
            self.size -= 1
            self.cache.pop(self.tail.key)
            self.tail = self.tail.left
            self.tail.right = None


if __name__ == '__main__':

    cases = [
        {
            "size": 2,
            "data": [
                {"f": "put", "args": [1, 1], "res": None},
                {"f": "put", "args": [2, 2], "res": None},
                {"f": "get", "args": [1], "res": 1},
                {"f": "put", "args": [3, 3], "res": None},
                {"f": "get", "args": [2], "res": -1},
                {"f": "put", "args": [4, 4], "res": None},
                {"f": "get", "args": [1], "res": -1},
                {"f": "get", "args": [3], "res": 3},
                {"f": "get", "args": [4], "res": 4},
            ],
        },
        {
            "size": 3,
            "data": [
                {"f": "put", "args": [1, 1], "res": None},
                {"f": "put", "args": [2, 2], "res": None},
                {"f": "put", "args": [3, 3], "res": None},
                {"f": "put", "args": [4, 4], "res": None},
                {"f": "get", "args": [4], "res": 4},
                {"f": "get", "args": [3], "res": 3},
                {"f": "get", "args": [2], "res": 2},
                {"f": "get", "args": [1], "res": -1},
                {"f": "put", "args": [5, 5], "res": None},
                {"f": "get", "args": [1], "res": -1},
                {"f": "get", "args": [2], "res": 2},
                {"f": "get", "args": [3], "res": 3},
                {"f": "get", "args": [4], "res": -1},
                {"f": "get", "args": [5], "res": 5},
            ],
        },
    ]
    for c in cases:
        lru = LRUCache(c["size"])
        print(lru.cap)
        for d in c["data"]:
            print(d)
            f = getattr(lru, d["f"])
            res = f(*d["args"])
            assert res == d["res"], (
                "expected: {}, got: {}".format(d["res"], res),
            )
