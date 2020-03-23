# Definition for singly-linked list.
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


# 定义两个指针，快指针，慢指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False



def output_linklist(link):
    while link:
        print(link.val)
        link = link.next


def input_linklist(*val):
    prehead = ListNode(0)
    result = prehead
    for i in val:
        prehead.next = ListNode(i)
        prehead = prehead.next
    return result.next


x = input_linklist(1, 2, 2, 1)
s = Solution()
print(s.hasCycle(x))

