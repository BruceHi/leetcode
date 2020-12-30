# 剑指 offer 18. 删除链表的节点
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pre = dummy = ListNode(0)
        dummy.next = head
        while pre.next:
            cur = pre.next
            if cur.val == val:
                pre.next = cur.next
                break
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
head = generate_link([4, 5, 1, 9])
print_link(s.deleteNode(head, 5))


head = generate_link([4, 5, 1, 9])
print_link(s.deleteNode(head, 1))
