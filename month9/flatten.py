# 430. 扁平化多级双向链表
# Definition for a Node.
import pkg_resources


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:

    # def flatten(self, head: 'Node') -> 'Node':
    #     dummy = Node(0, None, head, None)
    #     cur = head
    #     while cur:
    #         if not cur.child:
    #             cur = cur.next
    #         else:
    #             nxt = cur.next
    #             chead = self.flatten(cur.child)
    #
    #             # 连接前面
    #             cur.next = chead
    #             chead.prev = cur
    #             cur.child = None
    #
    #             # 定位到支链的最后
    #             while cur.next:
    #                 cur = cur.next
    #
    #             cur.next = nxt
    #
    #             # 若nxt 存在
    #             if nxt:
    #                 nxt.prev = cur
    #             cur = cur.next
    #     return dummy.next

    def flatten(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            if cur.child:
                nxt = cur.next
                other = self.flatten(cur.child)

                # 连接前面
                cur.next = other
                other.prev = cur
                cur.child = None

                # 定位到支链的最后
                while cur.next:
                    cur = cur.next

                cur.next = nxt

                # 若nxt 存在
                if nxt:
                    nxt.prev = cur
            cur = cur.next
        return head
