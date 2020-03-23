# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(3)
S = Solution()
y = S.reverseList(x)
print(y.val, y.next.val, y.next.next.val)
