# 判断是否为环形链表
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# # 使用set集合
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         record = set()
#         while head:
#             if head in record:
#                 return True
#             else:
#                 record.add(head)
#             head = head.next
#         return False

#
# # 定义两个指针，快指针，慢指针
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         slow, fast = head, head
#         while fast and fast.next:
#             slow, fast = slow.next, fast.next.next
#             if slow is fast:
#                 return True
#         return False

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False


def generate_link(nums: List[int]) -> ListNode:
    head = ListNode(0)
    cur = head
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return head.next


x = generate_link([1, 2, 2, 1])
s = Solution()
print(s.hasCycle(x))
