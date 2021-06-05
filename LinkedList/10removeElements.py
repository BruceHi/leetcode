# 删除链表中等于给定值 val 的所有节点。
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     pre, cur = dummy, head
    #     while cur:
    #         if cur.val == val:
    #             pre.next = cur.next
    #         else:
    #             pre = pre.next
    #         cur = cur.next
    #     return dummy.next

    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    #     pre = dummy = ListNode(0)
    #     dummy.next = head
    #     while pre.next:
    #         cur = pre.next
    #         if cur.val == val:
    #             pre.next = cur.next
    #         else:
    #             pre = pre.next
    #     return dummy.next

    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    #     pre = dummy = ListNode(0)
    #     cur = dummy.next = head
    #
    #     while cur:
    #         if cur.val == val:
    #             pre.next = cur.next
    #         else:
    #             pre = pre.next
    #         cur = cur.next
    #     return dummy.next

    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    #     pre = dummy = ListNode(0)
    #     dummy.next = head
    #
    #     while pre.next:
    #         cur = pre.next
    #         if cur.val == val:
    #             pre.next = cur.next
    #         else:
    #             pre = pre.next
    #     return dummy.next

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = dummy = ListNode(0)
        dummy.next = head

        while pre.next:
            cur = pre.next
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
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
a = generate_link([1, 2, 6, 3, 4, 5, 6])
print_link(s.removeElements(a, 6))

a = generate_link([2, 2, 2])
print_link(s.removeElements(a, 2))
