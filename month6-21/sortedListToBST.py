# 109. 有序链表转换为二叉搜索树

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def sortedListToBST(self, head: ListNode) -> TreeNode:
    #     nums = []
    #     while head:
    #         nums.append(head.val)
    #         head = head.next
    #
    #     def array_BST(nums):
    #         if not nums:
    #             return
    #         mid = len(nums) >> 1
    #         root = TreeNode(nums[mid])
    #         root.left = array_BST(nums[:mid])
    #         root.right = array_BST(nums[mid+1:])
    #         return root
    #
    #     return array_BST(nums)

    # 直接使用链表，失败，这种写法递归次数太长
    # def sortedListToBST(self, head: ListNode) -> TreeNode:
    #     if not head:
    #         return
    #     pre = None
    #     slow, fast = head, head
    #     while fast and fast.next:
    #         pre = slow
    #         slow, fast = slow.next, fast.next.next
    #
    #     # 断开
    #     if pre:  # 排除只包含单节点的情况
    #         pre.next = None
    #
    #     root = TreeNode(slow.val)
    #     root.left = self.sortedListToBST(head)  # 遇到单节点时，会重复递归单节点
    #     root.right = self.sortedListToBST(slow.next)
    #     return root

    # def sortedListToBST(self, head: ListNode) -> TreeNode:
    #     if not head:
    #         return
    #     pre = head
    #     slow, fast = head, head
    #     while fast and fast.next:
    #         pre = slow
    #         slow, fast = slow.next, fast.next.next
    #
    #     root = TreeNode(slow.val)
    #     if slow is fast:
    #         return root
    #
    #     pre.next = None
    #
    #     root.left = self.sortedListToBST(head)
    #     root.right = self.sortedListToBST(slow.next)
    #     return root

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        pre = None
        slow, fast = head, head
        while fast and fast.next:
            pre = slow
            slow, fast = slow.next, fast.next.next

        root = TreeNode(slow.val)

        # 断开
        if pre:  # 排除只包含单节点的情况
            pre.next = None
            root.left = self.sortedListToBST(head)

        root.right = self.sortedListToBST(slow.next)
        return root
