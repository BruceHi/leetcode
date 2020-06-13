# 合并两个有序链表
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         prehead = ListNode(0)
#         result = prehead
#         while l1 and l2:
#             if l1.val < l2.val:  # 从l1开始，不能是<=，相等的时候就该换一个。
#                 prehead.next = l1
#                 l1 = l1.next
#             else:
#                 prehead.next = l2
#                 l2 = l2.next
#             prehead = prehead.next
#         if l1:
#             prehead.next = l1
#         if l2:
#             prehead.next = l2
#         return result.next


class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     dummy = ListNode(0)
    #     cur = dummy
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             cur.next = l1
    #             l1 = l1.next
    #         else:
    #             cur.next = l2
    #             l2 = l2.next
    #         cur = cur.next
    #     cur.next = l1 if l1 else l2
    #
    #     return dummy.next

    # 递归
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2


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


x = generate_link([1, 2, 4])
y = generate_link([1, 3, 4])
s = Solution()
head = s.mergeTwoLists(x, y)
print_link(head)
