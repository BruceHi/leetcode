#  K 个一组翻转链表
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    #     cur = head
    #     for _ in range(k):
    #         if not cur:
    #             return head
    #         cur = cur.next
    #
    #     pre, cur = None, head
    #     for _ in range(k):
    #         cur.next, pre, cur = pre, cur, cur.next
    #     head.next = self.reverseKGroup(cur, k)
    #     return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def revrese(head, k):
            pre, cur = None, head
            for _ in range(k):
                cur.next, pre, cur = pre, cur, cur.next
            return pre, head

        pre = dummy = ListNode(0)
        dummy.next = head
        while pre.next:
            cur = pre.next
            for _ in range(k):
                if not cur:
                    return dummy.next
                cur = cur.next
            pre.next, pre = revrese(pre.next, k)
            pre.next = cur
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


s = Solution()
head = generate_link([1, 2, 3, 4, 5])
print_link(s.reverseKGroup(head, 2))

head = generate_link([1, 2, 3, 4, 5])
print_link(s.reverseKGroup(head, 3))

head = generate_link([1, 2, 3, 4, 5])
print_link(s.reverseKGroup(head, 5))
