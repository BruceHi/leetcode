# 143. 重排链表
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 中心节点,翻转,拼接
    # def reorderList(self, head: ListNode) -> None:
    #     slow = fast = dummy = ListNode(0)
    #     dummy.next = head
    #     while fast and fast.next:
    #         slow, fast = slow.next, fast.next.next
    #
    #     cur = slow.next
    #     slow.next = None  # 前半段要断开
    #
    #     pre = None
    #     while cur:
    #         cur.next, pre, cur = pre, cur, cur.next
    #
    #     l1, l2 = head, pre
    #     cur = dummy
    #     while l1 or l2:
    #         if l1:
    #             cur.next = l1
    #             cur = cur.next
    #             l1 = l1.next
    #         if l2:
    #             cur.next = l2
    #             cur = cur.next
    #             l2 = l2.next


    # def reorderList(self, head: ListNode) -> None:
    #     if not head:
    #         return
    #     slow, fast = head, head
    #     while fast.next and fast.next.next:
    #         slow, fast = slow.next, fast.next.next
    #     cur = slow.next
    #     slow.next = None
    #
    #     pre = None
    #     while cur:
    #         cur.next, pre, cur = pre, cur, cur.next
    #
    #     l1, l2 = head, pre
    #     while l1 and l2:
    #         l1.next, l1 = l2, l1.next
    #         l2.next, l2 = l1, l2.next

    # 线性表
    # def reorderList(self, head: ListNode) -> None:
    #     if not head:
    #         return
    #     nodes = []
    #     cur = head
    #     while cur:
    #         nodes.append(cur)
    #         cur = cur.next
    #
    #     cur = ListNode(0)
    #     i, j = 0, len(nodes) - 1
    #     while i <= j:
    #         cur.next = nodes[i]
    #         cur = cur.next
    #         cur.next = nodes[j]
    #         cur = cur.next
    #         i, j = i+1, j-1
    #     cur.next = None  # 去掉循环

    # def reorderList(self, head: ListNode) -> None:
    #     if not head:
    #         return
    #     nodes = []
    #     cur = head
    #     while cur:
    #         nodes.append(cur)
    #         cur = cur.next
    #
    #     i, j = 0, len(nodes) - 1
    #     while i < j:
    #         nodes[i].next = nodes[j]
    #         i += 1
    #         if i == j:  # 偶数个节点
    #             break
    #         nodes[j].next = nodes[i]
    #         j -= 1
    #     nodes[i].next = None  # 退出循环 i == j

    # 递归
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        cur = head
        while cur.next:
            cur = cur.next



def generate_link(nums: List[int]) -> ListNode:
    head = ListNode(0)
    cur = head
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return head.next


def print_link(head: ListNode) -> None:
    res, cur = [], head
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


s = Solution()
head = generate_link([1, 2, 3, 4])
s.reorderList(head)
print_link(head)

head = generate_link([1, 2, 3, 4, 5])
s.reorderList(head)
print_link(head)
