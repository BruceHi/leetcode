# 奇偶链表，奇在前面，原地
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 在原链表上进行删除插入操作
    # def oddEvenList(self, head: ListNode) -> ListNode:
    #     if not head or not head.next:
    #         return head
    #     pre, pre2, cur = head, head.next, head.next.next
    #     while cur:
    #         if cur.next:  # 偶
    #             tmp1, tmp2 = pre2.next.next, cur.next.next
    #             pre2.next, cur.next, pre.next = cur.next, pre.next, cur
    #             pre, pre2, cur = pre.next, tmp1, tmp2
    #         else:  # 奇
    #             pre2.next, cur.next, pre.next = cur.next, pre.next, cur
    #             cur = None
    #     return head

    # def oddEvenList(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return head
    #     odd, even, even_head = head, head.next, head.next
    #     while even and even.next:
    #         odd.next, even.next = even.next, even.next.next
    #         odd, even = odd.next, even.next
    #     odd.next = even_head
    #     return head

    # def oddEvenList(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return head
    #     odd, even, even_head = head, head.next, head.next
    #     while even and even.next:
    #         odd.next, even.next = even.next, even.next.next
    #         odd, even = odd.next, even.next
    #     odd.next = even_head
    #     return head

    # def oddEvenList(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return
    #     odd, even, even_head = head, head.next, head.next
    #     while even and even.next:
    #         odd.next, even.next = even.next, even.next.next
    #         odd, even = odd.next, even.next
    #     odd.next = even_head
    #     return head

    # def oddEvenList(self, head: ListNode) -> ListNode:
    #     odd_head, even_head = ListNode(0), ListNode(0)
    #     o_cur, e_cur = odd_head, even_head
    #
    #     flag = 1
    #     while head:
    #         if flag & 1:
    #             o_cur.next = head
    #             o_cur = o_cur.next
    #         else:
    #             e_cur.next = head
    #             e_cur = e_cur.next
    #         flag += 1
    #         tmp = head.next
    #         head.next = None
    #         head = tmp
    #
    #     o_cur.next = even_head.next
    #     return odd_head.next


    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        odd, even, even_head = head, head.next, head.next
        while even and even.next:
            odd.next, even.next = even.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = even_head
        return head


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
a = generate_link([1, 2, 3, 4, 5])
print_link(s.oddEvenList(a))

a = generate_link([2, 1, 3, 5, 6, 4, 7])
print_link(s.oddEvenList(a))

a = generate_link([1, 2, 3, 4])  # 偶可以
print_link(s.oddEvenList(a))
