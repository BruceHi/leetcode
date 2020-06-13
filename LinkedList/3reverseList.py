from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def reverseList(self, head: ListNode) -> ListNode:
#         pre, cur = None, head
#         while cur:
#             cur.next, pre, cur = pre, cur, cur.next
#         return pre
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
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


# x = ListNode(1)
# x.next = ListNode(2)
# x.next.next = ListNode(3)
x = generate_link([1, 2, 3])
S = Solution()
y = S.reverseList(x)
# print(y.val, y.next.val, y.next.next.val)
print_link(y)
