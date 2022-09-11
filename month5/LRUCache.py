# LRU 缓存
# 其中只有 key 和 value 同时相等，才能看作同一个结点
# key 存在则更改 value


# # 双链表方法
# class ListNode:
#     def __init__(self, x, y):
#         self.key, self.val = x, y
#         self.prev, self.next = None, None
#
#
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.size = 0
#         self.head, self.tail = ListNode(None, None), ListNode(None, None)
#         self.head.next = self.tail
#         self.tail.prev = self.head
#
#     def get(self, key: int) -> int:
#         curr = self.head
#         for _ in range(self.size):
#             curr = curr.next
#             if curr.key == key:
#                 # 删除结点
#                 pred, succ = curr.prev, curr.next
#                 pred.next, succ.prev = succ, pred
#                 pred, succ = self.head, self.head.next
#                 # 头部添加结点
#                 curr.next, curr.prev = succ, pred
#                 pred.next, succ.prev = curr, curr
#                 return curr.val
#
#         return -1
#
#     def put(self, key: int, value: int) -> None:
#         # 没找到 key
#         if self.get(key) == -1:
#             self.size += 1
#             new_node = ListNode(key, value)
#             pred, succ = self.head, self.head.next
#             new_node.next, new_node.prev = succ, pred
#             pred.next, succ.prev = new_node, new_node
#
#             if self.size > self.capacity:
#                 self.size -= 1
#                 pred, succ = self.tail.prev.prev, self.tail
#                 pred.next, succ.prev = succ, pred
#
#         # 找到了 key, 但值不同。已经访问过了，位于最前面。注意使用 elif
#         elif self.get(key) != value:
#             self.head.next.val = value


# 使用有序字典：OrderedDict
from collections import OrderedDict

#
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.dic = OrderedDict()
#         self.capacity = capacity
#         self.size = 0
#
#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
#         res = self.dic.pop(key)
#         self.dic[key] = res
#         return res
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             self.dic.pop(key)
#         else:
#             self.size += 1
#             if self.size > self.capacity:
#                 self.size -= 1
#                 self.dic.popitem(last=False)
#         self.dic[key] = value

# class LRUCache(OrderedDict):
#
#     def __init__(self, capacity: int):
#         super().__init__()
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         self.move_to_end(key)
#         return self[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)


# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.dic = OrderedDict()
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
#         self.dic.move_to_end(key)
#         return self.dic[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             self.dic.move_to_end(key)
#         self.dic[key] = value
#         if len(self.dic) > self.capacity:
#             self.dic.popitem(last=False)

# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.dic = OrderedDict()
#
#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
#         self.dic.move_to_end(key)
#         return self.dic[key]
#
#     # 三者情况：key 不在；key 在 值不同；key 在值相同
#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             self.dic.move_to_end(key)
#         self.dic[key] = value
#         if len(self.dic) > self.capacity:
#             self.dic.popitem(False)




# 由于涉及到前面删除，后面插入，尤其是后面插入（需要前面节点）的处理，所以使用双链表
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.head = ListNode()
#         self.tail = self.head
#         self.capacity = capacity + 2
#
#
#     def get(self, key: int) -> int:
#         pre = self.head
#         while pre.next:
#             cur = pre.next
#             if cur.key == key:
#                 pre.next = cur.next
#
#
#     def put(self, key: int, value: int) -> None:


class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.head = ListNode()
#         self.tail = ListNode()
#         self.head.next, self.tail.prev = self.tail, self.head
#         self.remain = capacity
#
#     def get(self, key: int) -> int:
#         pre = self.head
#         while pre.next:
#             cur = pre.next
#             if key == cur.key:
#                 end = cur.next
#                 pre.next, end.prev = end, pre
#                 first = self.tail.prev
#                 first.next, self.tail.prev = cur, cur
#                 cur.prev, cur.next = first, self.tail
#                 return cur.val
#             pre = pre.next
#         return -1
#
#     def put(self, key: int, value: int) -> None:
#         flag = 0
#         cur = self.head
#         while cur:
#             if cur.key == key:
#                 flag = 1
#                 break
#             cur = cur.next
#
#         # 不在
#         if not flag:
#             if self.remain == 0:
#                 end = self.head.next.next
#                 self.head.next, end.prev = end, self.head
#                 self.remain += 1
#             node = ListNode(key, value)
#             first = self.tail.prev
#             first.next, self.tail.prev = node, node
#             node.prev, node.next = first, self.tail
#             self.remain -= 1
#
#         # 在
#         self.get(key)
#         self.tail.prev.val = value

# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.dic = {}  # 用来判断是否存在 元素 key:node，用于查看 key 是否存在，顺便找到 node，不用再变量一遍
#         self.head = ListNode()
#         self.tail = ListNode()
#         self.head.next, self.tail.prev = self.tail, self.head
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
#         node = self.dic[key]
#         self.move_to_tail(node)
#         return node.val
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             node = self.dic[key]
#             node.val = value
#             self.move_to_tail(node)
#         else:
#             node = ListNode(key, value)
#             self.dic[key] = node
#             self.add_to_tail(node)
#             if len(self.dic) > self.capacity:
#                 removed = self.remove_head()
#                 self.dic.pop(removed.key)
#
#     def move_to_tail(self, node):
#         self.remove_node(node)
#         self.add_to_tail(node)
#
#     def add_to_tail(self, node):
#         first = self.tail.prev
#         first.next, self.tail.prev = node, node
#         node.prev, node.next = first, self.tail
#
#     def remove_head(self):
#         node = self.head.next
#         self.remove_node(node)
#         return node
#
#     def remove_node(self, node):
#         # 教训，双向链表 中的 perv 千万别写成 pre
#         a, b = node.prev, node.next
#         a.next, b.prev = b, a
#
#         # node.prev.next = node.next
#         # node.next.prev = node.prev
#
#         # node.prev.next, node.next.prev = node.next, node.prev


# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.dic = OrderedDict()
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
#         self.dic.move_to_end(key)
#         return self.dic[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             self.dic.move_to_end(key)
#         self.dic[key] = value
#         if len(self.dic) > self.capacity:
#             self.dic.popitem(last=False)


# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.dic = OrderedDict()
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
#         self.dic.move_to_end(key)
#         return self.dic[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             self.dic.move_to_end(key)
#         self.dic[key] = value
#         if len(self.dic) > self.capacity:
#             self.dic.popitem(last=False)

# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.dic = OrderedDict()
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
#         self.dic.move_to_end(key)
#         return self.dic[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             self.dic.move_to_end(key)
#         self.dic[key] = value
#         if len(self.dic) > self.capacity:
#             self.dic.popitem(last=False)

# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.dic = OrderedDict()
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
#         self.dic.move_to_end(key)
#         return self.dic[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             self.dic.move_to_end(key)
#         self.dic[key] = value
#         if len(self.dic) > self.capacity:
#             self.dic.popitem(last=False)

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)



def print_link(head: ListNode) -> None:
    res, cur = [], head
    while cur:
        res.append((cur, cur.val, cur.key, cur.prev, cur.next))
        cur = cur.next
    print(res)


# cache = LRUCache(2)
#
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))  # 返回  1
# cache.put(3, 3)  # 该操作会使得密钥 2 作废
# print(cache.get(2))  # 返回 -1 (未找到)
# cache.put(4, 4)  # 该操作会使得密钥 1 作废
# print(cache.get(1))  # 返回 -1 (未找到)
# print(cache.get(3))  # 返回  3
# print(cache.get(4))  # 返回  4
#
# print("------------------")
#
# cache = LRUCache(2)
# print(cache.get(2))
# cache.put(2, 6)
# print(cache.get(1))
# cache.put(1, 5)
# cache.put(1, 2)
# print(cache.get(1))
# print(cache.get(2))
#
# print("--------------")
# # [null,null,null,null,null,-1,3]
# cache = LRUCache(2)
# cache.put(2, 1)
# cache.put(1, 1)
# cache.put(2, 3)
# cache.put(4, 1)
# print(cache.get(1))
# print(cache.get(2))

def print_func(funs, attrs):
    res = [None]
    obj = eval(funs[0])(*attrs[0])
    for f, a in zip(funs[1:], attrs[1:]):
        res.append(getattr(obj, f)(*a))
    print(res)


funs = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
attrs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
print_func(funs, attrs)