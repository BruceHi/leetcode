# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        node.val, node.next = node.next.val, node.next.next


# class PrintNode():
#   '''''
#   输出指定节点为起始节点的链表
#   '''
#   def print_node(self,node):
#     res_list=[]
#     while node:
#       res_list.append(str(node.num))
#       node=node.next
#     print('->'.join(res_list))

# head = [4,5,1,9]
# p = 5
# node = ListNode(head)
# print(node)
# # s = Solution()
# # s.deleteNode(p)



