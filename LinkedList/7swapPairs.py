# 两两交换链表的结点
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def swapPairs(self, head: ListNode) -> ListNode:
    #     pre = dummy = ListNode(0)
    #     dummy.next = head
    #     while pre.next and pre.next.next:
    #         a, b = pre.next, pre.next.next
    #         pre.next, b.next, a.next = b, a, b.next
    #         pre = a
    #     return dummy.next

    # def swapPairs(self, head: ListNode) -> ListNode:
    #     if not head or not head.next:
    #         return head
    #     a, b = head, head.next
    #     b.next, a.next = a, self.swapPairs(b.next)
    #     return b

    def swapPairs(self, head: ListNode) -> ListNode:
        pre = dummy = ListNode(0)
        pre.next = cur = head
        while cur and cur.next:
            tmp = cur.next
            pre.next, tmp.next, cur.next = tmp, cur, tmp.next
            pre, cur = cur, cur.next
        return dummy.next


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


x = generate_link([1, 2, 3, 4])
s = Solution()
print_link(s.swapPairs(x))
