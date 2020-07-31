# 合并 k 个排序链表
from typing import List
from functools import reduce
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __lt__(self, other):
    #     return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val


class Solution:

    # 一个一个地合并
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     def merge(node1, node2):
    #         cur = dummy = ListNode(0)
    #         while node1 and node2:
    #             if node1.val <= node2.val:
    #                 cur.next = node1
    #                 node1 = node1.next
    #             else:
    #                 cur.next = node2
    #                 node2 = node2.next
    #             cur = cur.next
    #         cur.next = node1 if node1 else node2
    #         return dummy.next
    #
    #     if lists:
    #         return reduce(merge, lists)

    # # 分治法
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     return self.merge(lists, 0, len(lists) - 1)
    #
    # def merge(self, lists, left, right):
    #     if left == right:
    #         return lists[left]
    #     if left < right:
    #         mid = left + right >> 1
    #         return self.mergeTwoList(self.merge(lists, left, mid), self.merge(lists, mid+1, right))
    #
    # def mergeTwoList(self, l1, l2):
    #     if not l1:
    #         return l2
    #     if not l2:
    #         return l1
    #     if l1.val < l2.val:
    #         l1.next = self.mergeTwoList(l1.next, l2)
    #         return l1
    #     l2.next = self.mergeTwoList(l1, l2.next)
    #     return l2

    # # 堆，取出所有结点维护一个堆。空间复杂度是 O（n）,时间复杂度是 n log n
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     if not lists:
    #         return
    #     queue = []
    #     cur = dummy = ListNode(0)
    #     for node in lists:
    #         while node:
    #             heapq.heappush(queue, (node.val, node))  # 需要 ListNode 构造加上 _lt_
    #             node = node.next
    #     while queue:
    #         _, cur.next = heapq.heappop(queue)
    #         cur = cur.next
    #     return dummy.next

    # 使用 堆的正确方法，空间复杂度是 O（k）,时间复杂度是 n log k
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        queue = []
        cur = dummy = ListNode(0)
        for node in lists:
            if node:
                heapq.heappush(queue, node)  # 同样需要 ListNode 构造加上 _lt_

        while queue:
            head = heapq.heappop(queue)
            cur.next = head
            cur = cur.next
            if head.next:
                heapq.heappush(queue, head.next)
        return dummy.next

    # 堆，不考虑改变构造方法
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     if not lists:
    #         return
    #     queue = []
    #     cur = dummy = ListNode(0)
    #     for i, node in enumerate(lists):
    #         if node:
    #             heapq.heappush(queue, (node.val, i))
    #             lists[i] = lists[i].next  # 相等于重新引导链表的根节点往后移一位
    #
    #     while queue:
    #         val, idx = heapq.heappop(queue)
    #         cur.next = ListNode(val)
    #         cur = cur.next
    #         if lists[idx]:
    #             heapq.heappush(queue, (lists[idx].val, idx))
    #             lists[idx] = lists[idx].next
    #     return dummy.next

    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     if not lists:
    #         return
    #     queue = []
    #     cur = dummy = ListNode(0)
    #     for i, node in enumerate(lists):
    #         if node:
    #             heapq.heappush(queue, (node.val, i))
    #
    #     while queue:
    #         val, idx = heapq.heappop(queue)
    #         cur.next = ListNode(val)
    #         cur = cur.next
    #         if lists[idx].next:
    #             heapq.heappush(queue, (lists[idx].next.val, idx))
    #             lists[idx] = lists[idx].next
    #     return dummy.next


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
a = generate_link([1, 4, 5])
b = generate_link([1, 2, 4])
c = generate_link([3])
print_link(s.mergeKLists([a, b, c]))

# c = generate_link([])
print_link(s.mergeKLists([]))
