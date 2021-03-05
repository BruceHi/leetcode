# 147. 对链表进行插入排序
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # # 使用数组
    # def insertionSortList(self, head: ListNode) -> ListNode:
    #     cur = head
    #     nodes = []
    #     while cur:
    #         nodes.append(cur)
    #         cur = cur.next
    #
    #     nodes.sort(key=lambda x:x.val)
    #     cur = dummy = ListNode(0)
    #     for node in nodes:
    #         cur.next = node
    #         cur = cur.next
    #     cur.next = None
    #     return dummy.next

    # 插入排序
    def insertionSortList(self, head: ListNode) -> ListNode:
        pre = dummy = ListNode(float('-inf'))  # 注意这个
        # print(dummy.val)
        dummy.next = head
        while pre.next:
            cur = pre.next
            if cur.val < pre.val:
                find = dummy  # 找到要插入的前驱节点
                while find.next.val < cur.val:
                    find = find.next
                pre.next = cur.next  # 相当于 pre 指针向后移位
                find.next, cur.next = cur, find.next
            else:
                pre = pre.next
        return dummy.next



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
head = generate_link([4, 2, 1, 3])
print_link(s.insertionSortList(head))

head = generate_link([-1, 5, 3, 4, 0])
print_link(s.insertionSortList(head))
