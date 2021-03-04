# 剑指 offer 22. 链表中倒数第 k 个节点
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next
        return slow



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
print_link(s.getKthFromEnd(a, 2))
