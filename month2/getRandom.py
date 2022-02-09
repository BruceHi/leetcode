# 382. 链表随机节点
from random import choice
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # def __init__(self, head: Optional[ListNode]):
    #     self.head = head
    #     self.val = self.get_val()
    #
    # def get_val(self):
    #     res, cur = [], self.head,
    #     while cur:
    #         res.append(cur.val)
    #         cur = cur.next
    #     return res
    #
    # def getRandom(self) -> int:
    #     return choice(self.val)

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return choice(self.arr)



def print_link(head: ListNode):
    res, cur = [], head,
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


def generate_link(nums):
    cur = head = ListNode(0)
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return head.next


head = generate_link([1, 2, 3])
s = Solution(head)
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
