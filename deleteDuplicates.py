# 83. 删除排序链表中的重复元素
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     pre = dummy = ListNode(None)  # 不能使用 0，参见第3个示例
    #     dummy.next = head
    #     while pre.next:
    #         cur = pre.next
    #         if cur.val == pre.val:
    #             pre.next = cur.next
    #         else:
    #             pre = pre.next
    #     return dummy.next

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        pre = head
        while pre.next:
            cur = pre.next
            if cur.val == pre.val:
                pre.next = cur.next
            else:
                pre = pre.next
        return head


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
head = generate_link([1, 1, 3])
print_link(s.deleteDuplicates(head))

head = generate_link([1, 1, 2, 3, 3])
print_link(s.deleteDuplicates(head))

head = generate_link([0,0,0,0,0])
print_link(s.deleteDuplicates(head))

head = generate_link([])
print_link(s.deleteDuplicates(head))
