# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(0)
        result = prehead
        while l1 and l2:
            if l1.val < l2.val:  # 从l1开始，不能是<=，相等的时候就该换一个。
                prehead.next = l1
                l1 = l1.next
            else:
                prehead.next = l2
                l2 = l2.next
            prehead = prehead.next
        if l1:
            prehead.next = l1
        if l2:
            prehead.next = l2
        return result.next


def output_linklist(link):
    while link:
        print(link.val)
        link = link.next


x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(4)
y = ListNode(1)
y.next = ListNode(3)
y.next.next = ListNode(4)
# input_linklist(x)
s = Solution()
new_listNode = s.mergeTwoLists(x, y)
output_linklist(new_listNode)

# print(new_listNode.val, new_listNode.next.val, new_listNode.next.next.val)