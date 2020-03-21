# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 需要自己添加哑节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        dummy = ListNode(0)
        dummy.next = head

        first = head
        length = 0
        while not first:
            length += 1
            first = first.next

        first = dummy
        for _ in range(length-n):
            first = first.next

        first.next = first.next.next
        return dummy.next



