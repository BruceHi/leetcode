# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(0)
        pre.next = head
        result = pre
        # pre, pre.next = self, head
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return result.next


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


x = input_linklist(1, 2, 3, 4)
s = Solution()
output_linklist(s.swapPairs(x))