# 相交链表，返回相交结点，若无交点，返回 None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # set 记录
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     record = set()
    #     cur = headA
    #     while cur:
    #         record.add(cur)
    #         cur = cur.next
    #     cur = headB
    #     while cur:
    #         if cur in record:
    #             return cur
    #         cur = cur.next

    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     if not headA or not headB:
    #         return
    #     cur1, cur2 = headA, headB
    #     while cur1 != cur2:
    #         # 每次只允许走一步，下面的就是走了两步
    #         # if not cur1:
    #         #     cur1 = headB
    #         # if not cur2:
    #         #     cur2 = headA
    #         # cur1, cur2 = cur1.next, cur2.next
    #         cur1 = cur1.next if cur1 else headB
    #         cur2 = cur2.next if cur2 else headA
    #     return cur1

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1, cur2 = headA, headB
        while cur1 != cur2:
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA
        return cur1
