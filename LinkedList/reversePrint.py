# 剑指 offer 06. 从尾到头打印链表
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # # 普通方法
    # def reversePrint(self, head: ListNode) -> List[int]:
    #     res = []
    #     while head:
    #         res.append(head.val)
    #         head = head.next
    #     res.reverse()
    #     return res

    # 递归
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []




def generate_link(nums):
    cur = dummy = ListNode(0)
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next


def print_link(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


s = Solution()
head = generate_link([1, 2, 3])
print_link(head)
print(s.reversePrint(head))