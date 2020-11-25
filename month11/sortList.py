# 148. 排序链表
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # # 必须把原来的链接断开
    # def sortList(self, head: ListNode) -> ListNode:
    #     nodes = []
    #     pre = cur = head
    #     while cur:
    #         nodes.append(cur)
    #         cur = cur.next
    #         pre.next = None
    #         pre = cur
    #
    #     nodes.sort(key=lambda x: x.val)
    #     cur = dummy = ListNode(0)
    #     for node in nodes:
    #         cur.next = node
    #         cur = cur.next
    #     return dummy.next

    # # 不断开，只修改原来链表的结尾，空间复杂度为 O(n)。
    # def sortList(self, head: ListNode) -> ListNode:
    #     nodes = []
    #     cur = head
    #     while cur:
    #         nodes.append(cur)
    #         cur = cur.next
    #
    #     nodes.sort(key=lambda x: x.val)
    #     cur = dummy = ListNode(0)
    #     for node in nodes:
    #         cur.next = node
    #         cur = cur.next
    #     cur.next = None  # 这是关键一步，否则由于原来链表的影响，可能会成环。
    #     return dummy.next

    # 归并排序，空间复杂度为 O(log n)
    # 对数组做归并排序的空间复杂度为 O(n)，分别由新开辟数组O(n)和递归函数调用栈 O(logn)组成。
    # 数组额外空间：链表可以通过修改引用来更改节点顺序，无需像数组一样开辟额外空间；
    # https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
    def sortList(self, head: ListNode) -> ListNode:
        def sort(head):
            if not head or not head.next:  # 空值，只有一个值
                return head
            slow, fast = head, head.next  # 对 3 个值 没有影响，主要影响两个值。特别注意这点。
            while fast and fast.next:
                fast, slow = fast.next.next, slow.next
            mid = slow.next
            slow.next = None
            return merge(sort(head), sort(mid))

        def merge(head1, head2):
            cur = dummy = ListNode(0)
            tmp1, tmp2 = head1, head2
            while tmp1 and tmp2:
                if tmp1.val < tmp2.val:
                    cur.next = tmp1
                    tmp1 = tmp1.next
                else:
                    cur.next = tmp2
                    tmp2 = tmp2.next
                cur = cur.next
            if tmp1:
                cur.next = tmp1
            if tmp2:
                cur.next = tmp2
            return dummy.next

        return sort(head)



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
head = generate_link([4,2,1,3])
print_link(s.sortList(head))

head = generate_link([-1,5,3,4,0])
print_link(s.sortList(head))

head = generate_link([])
print_link(s.sortList(head))

head = generate_link([1, 2])
print_link(s.sortList(head))