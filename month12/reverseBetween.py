# 92.反转链表2
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # # left 左断点的左边，right 左断点的右边
    # def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    #     left = dummy = ListNode(0)
    #     dummy.next = head
    #     for _ in range(m-1):
    #         left = left.next
    #     right = cur = left.next
    #     pre = None
    #     for _ in range(n-m+1):
    #         cur.next, pre, cur = pre, cur, cur.next
    #     left.next = pre
    #     right.next = cur
    #     return dummy.next

    # 采用像 swapPairs 那种的交换方式
    # def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    #     pre = dummy = ListNode(0)
    #     dummy.next = head
    #     for _ in range(m-1):
    #         pre = pre.next
    #     a = pre.next
    #     for _ in range(n-m):
    #         b = a.next
    #         pre.next, b.next, a.next = b, pre.next, b.next   # 注意这里 b.next 是连到 pre 之后的
    #     return dummy.next

    # def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    #     pre = dummy = ListNode(0)
    #     dummy.next = head
    #     for _ in range(left-1):
    #         pre = pre.next
    #     cur = pre.next
    #     a, b = None, pre.next
    #     for _ in range(right-left+1):
    #         b.next, a, b = a, b, b.next
    #     pre.next = a
    #     cur.next = b
    #     return dummy.next

    # def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    #     pre = dummy = ListNode(0)
    #     dummy.next = head
    #     for _ in range(left-1):
    #         pre = pre.next
    #     a = pre.next
    #     for _ in range(right-left):
    #         b = a.next
    #         pre.next, b.next, a.next = b, pre.next, b.next
    #     return dummy.next

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        pre = dummy = ListNode(0)
        dummy.next = head
        for _ in range(left-1):
            pre = pre.next

        cur = pre.next
        for _ in range(right-left):
            a, b = pre.next, cur.next
            pre.next, b.next, cur.next = b, a, b.next
        return dummy.next


def generate_link(nums):
    cur = dummy = ListNode(0)
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

def print_link(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


s = Solution()
head = generate_link([1, 2, 3, 4, 5])
print_link(s.reverseBetween(head, 2, 4))

head = generate_link([5])
print_link(s.reverseBetween(head, 1, 1))
