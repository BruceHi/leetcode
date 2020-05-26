# 检测是否有环。若有环返回入环结点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # # 双指针
    # def detectCycle(self, head: ListNode):
    #     slow, fast = head, head
    #     while fast and fast.next:
    #         slow, fast = slow.next, fast.next.next
    #         if slow is fast:
    #             find = head
    #             while find is not slow:
    #                 find, slow = find.next, slow.next
    #             return find
    #
    #     return

    # 记录
    def detectCycle(self, head: ListNode):
        record = set()
        node = head
        while node:
            if node in record:
                return node
            else:
                record.add(node)
            node = node.next
        return


