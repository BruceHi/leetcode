# 删除倒数第 n 个结点
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 需要自己添加哑节点
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int):
#         dummy = ListNode(0)
#         dummy.next = head
#
#         first = head
#         length = 0
#         while not first:
#             length += 1
#             first = first.next
#
#         first = dummy
#         for _ in range(length-n):
#             first = first.next
#
#         first.next = first.next.next
#         return dummy.next

class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     dummy = ListNode(0)
    #     dummy.next = head
    #
    #     first = head
    #     size = 0
    #     while first:
    #         size += 1
    #         first = first.next
    #
    #     pre = dummy
    #     for _ in range(size - n):
    #         pre = pre.next
    #     pre.next = pre.next.next
    #
    #     return dummy.next

    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     dummy = ListNode(0)
    #     dummy.next = head
    #
    #     left, right = dummy, dummy
    #     for _ in range(n+1):
    #         right = right.next
    #
    #     while right:
    #         left, right = left.next, right.next
    #
    #     left.next = left.next.next  # 遍历结束后，left 为前驱结点
    #     return dummy.next


# def output_linklist(link):  # 输出链表
#     res = link
#     while res:
#         print(res.val)
#         res = res.next

    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     cur = pre = dummy = ListNode(0)
    #     dummy.next = head
    #
    #     for _ in range(n+1):
    #         cur = cur.next
    #
    #     while cur:
    #         pre, cur = pre.next, cur.next
    #     pre.next = pre.next.next
    #
    #     return dummy.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = dummy = ListNode(0)
        dummy.next = head
        for _ in range(n+1):
            fast = fast.next

        pre = dummy
        while fast:
            pre, fast = pre.next, fast.next

        pre.next = pre.next.next
        return dummy.next




def print_link(head: ListNode):  # 打印链表
    res, cur = [], head,
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


# def input_link(*val):  # 构造带无头结点的链表，传入的参数必须是解包过的，如 1，2， 3， 4
#     prehead = ListNode(0)
#     result = prehead
#     for i in val:
#         prehead.next = ListNode(i)
#         prehead = prehead.next
#     return result.next

# def generate_link(nums: List[int]):  # 构造不带头结点的链表
#     head = ListNode(0)
#     cur = head
#     for num in nums:
#         cur.next = ListNode(num)
#         cur = cur.next
#     return head.next

def generate_link(*nums: int):
    cur = head = ListNode(0)
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return head.next



s = Solution()
# nums = [1, 2, 3, 4, 5]
# a = input_linklist(*nums)

# a = generate_link([1, 2, 3, 4, 5])
a = generate_link(1, 2, 3, 4, 5)
new = s.removeNthFromEnd(a, 2)
print_link(new)

a = generate_link(1)
new = s.removeNthFromEnd(a, 1)
print_link(new)