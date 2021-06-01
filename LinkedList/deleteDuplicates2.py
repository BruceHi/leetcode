# 82. 删除排序链表中的重复元素2
# 只保留出现一次的
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     pre = dummy = ListNode(0)
    #     dummy.next = head
    #     while pre.next:
    #         a = pre.next
    #         val = a.val
    #
    #         flag = 0  # 判断是否有重复的标志
    #         b = a.next
    #         while b and b.val == val:
    #             b = b.next
    #             flag = 1

    #         if flag:
    #             pre.next = b
    #         else:
    #             pre = a
    #     return dummy.next

    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     pre = dummy = ListNode(0)
    #     dummy.next = head
    #     while pre.next:
    #         a = pre.next
    #         val = a.val
    #
    #         # 前两种是不存在重复的
    #         if not a.next:
    #             pre = a
    #         elif a.next.val != val:
    #             pre = a
    #         else:
    #             b = a.next
    #             while b and b.val == val:
    #                 b = b.next
    #             pre.next = b
    #     return dummy.next

    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     pre = dummy = ListNode(0)
    #     dummy.next = head
    #     while pre.next:
    #         a = pre.next
    #         val = a.val
    #
    #         b = a.next
    #         if not b or b.val != val:
    #             pre = a  # 移动指针
    #         else:
    #             while b and b.val == val:
    #                 b = b.next
    #             pre.next = b
    #     return dummy.next

    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     pre = dummy = ListNode(0)
    #     dummy.next = head
    #     while pre.next:
    #         a = pre.next
    #         val = a.val
    #
    #         b = a.next
    #         if not b or b.val != val:
    #             pre = a  # 移动指针
    #         else:
    #             while b and b.val == val:
    #                 b = b.next
    #             pre.next = b
    #     return dummy.next

    # 官方题解没我自己写得好
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     pre = dummy = ListNode(0)
    #     dummy.next = head
    #     while pre.next and pre.next.next:
    #         a, b = pre.next, pre.next.next
    #         val = a.val
    #         if b.val != val:
    #             pre = a
    #         else:
    #             while b and b.val == val:
    #                 b = b.next
    #             pre.next = b
    #
    #     return dummy.next

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = dummy = ListNode(0)
        dummy.next = head

        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            num = a.val
            if b.val != num:
                pre = a
            else:
                while b and b.val == num:
                    b = b.next
                pre.next = b
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
head = generate_link([1, 2, 3, 3, 4, 4, 5])
print_link(s.deleteDuplicates(head))

head = generate_link([1, 1, 1, 2, 3])
print_link(s.deleteDuplicates(head))

head = generate_link([0, 0, 0, 0, 0])
print_link(s.deleteDuplicates(head))

head = generate_link([])
print_link(s.deleteDuplicates(head))
