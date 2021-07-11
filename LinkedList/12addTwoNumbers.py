# 两数相加
# 与 415 题相似
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     node = ListNode(0)
    #     cur = node
    #     flag = 0
    #     cur1, cur2 = l1, l2
    #
    #     while cur1 and cur2:
    #         num = cur1.val + cur2.val + flag
    #         if num > 9:
    #             num %= 10
    #             flag = 1
    #         else:
    #             flag = 0
    #         cur.next = ListNode(num)
    #         cur, cur1, cur2 = cur.next, cur1.next, cur2.next
    #
    #     while cur1:
    #         if not flag:
    #             cur.next = cur1
    #             break
    #         num = cur1.val + flag
    #         if num > 9:
    #             num %= 10
    #             flag = 1
    #         else:
    #             flag = 0
    #         cur.next = ListNode(num)
    #         cur, cur1 = cur.next, cur1.next
    #
    #     while cur2:
    #         if not flag:
    #             cur.next = cur2
    #             break
    #         num = cur2.val + flag
    #         if num > 9:
    #             num %= 10
    #             flag = 1
    #         else:
    #             flag = 0
    #         cur.next = ListNode(num)
    #         cur, cur2 = cur.next, cur2.next
    #
    #     if flag:
    #         cur.next = ListNode(1)
    #
    #     return node.next

    # # 改进
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     node = ListNode(0)
    #     cur = node
    #     flag, num = 0, 0
    #     cur1, cur2 = l1, l2
    #
    #     while cur1 or cur2:
    #         if cur1 and cur2:
    #             num = cur1.val + cur2.val + flag
    #             cur1, cur2 = cur1.next, cur2.next
    #         elif cur1 and not cur2:
    #             num = cur1.val + flag
    #             cur1 = cur1.next
    #         else:
    #             num = cur2.val + flag
    #             cur2 = cur2.next
    #
    #         if num > 9:
    #             num %= 10
    #             flag = 1
    #         else:
    #             flag = 0
    #         cur.next = ListNode(num)
    #         cur = cur.next
    #
    #     if flag:
    #         cur.next = ListNode(1)
    #
    #     return node.next

    # 改进 https://my.oschina.net/yves175/blog/827758
    # 若其后 l1、l2 不再使用，可以直接用他们遍历
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     cur = dummy = ListNode(0)
    #     s = 0  # 进位 或 和
    #     while l1 or l2 or s:
    #         s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
    #         cur.next = ListNode(s % 10)
    #         cur = cur.next
    #         s //= 10
    #         l1 = l1.next if l1 else None
    #         l2 = l2.next if l2 else None
    #     return dummy.next

    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     cur = dummy = ListNode(0)
    #     s = 0  # 每一轮循环过后 s 都是进位
    #     while l1 or l2 or s:
    #         s += (l1.val if l1 else 0) + (l2.val if l2 else 0)  # 和
    #         cur.next = ListNode(s % 10)
    #         cur = cur.next
    #         s //= 10
    #         l1 = l1.next if l1 else None
    #         l2 = l2.next if l2 else None
    #     return dummy.next

    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     cur = dummy = ListNode(0)
    #     s = 0
    #     while l1 or l2 or s:
    #         s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
    #         cur.next = ListNode(s % 10)
    #         cur = cur.next
    #         s //= 10
    #         l1 = l1.next if l1 else None
    #         l2 = l2.next if l2 else None
    #     return dummy.next

    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     carry = 0
    #     cur = dummy = ListNode(0)
    #     while l1 or l2 or carry:
    #         num = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
    #         carry = num // 10
    #         val = num % 10
    #         cur.next = ListNode(val)
    #         cur = cur.next
    #         if l1:
    #             l1 = l1.next
    #         if l2:
    #             l2 = l2.next
    #     return dummy.next

    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     cur = dummy = ListNode(0)
    #     carry = 0
    #     while l1 or l2 or carry:
    #         val = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
    #         carry = val // 10
    #         cur.next = ListNode(val % 10)
    #         cur = cur.next
    #         if l1:
    #             l1 = l1.next
    #         if l2:
    #             l2 = l2.next
    #     return dummy.next



    def addTwoNumbers(self, l1, l2):
        l1, l2 = reverse(l1), reverse(l2)
        cur = dummy = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry = val // 10
            cur.next = ListNode(val % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        a = dummy.next
        return reverse(dummy.next)


def reverse(head):
    pre, cur = None, head
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    return pre

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
a = generate_link([2, 4, 3])
b = generate_link([5, 6, 4])
print_link(s.addTwoNumbers(a, b))


a = generate_link([9, 9, 9])
b = generate_link([2, 1])
print_link(s.addTwoNumbers(a, b))

a = generate_link([1, 2, 5, 6])
b = generate_link([1, 5, 6])
print_link(s.addTwoNumbers(a, b))
