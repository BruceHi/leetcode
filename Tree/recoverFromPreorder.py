# 从先序遍历还原二叉树，不太好理解，日后再来做一做
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def recoverFromPreorder(self, S: str) -> TreeNode:
    #     path, i = [], 0
    #     while i < len(S):
    #         level = 0
    #         while S[i] == '-':
    #             level += 1
    #             i += 1
    #
    #         val = 0
    #         while i < len(S) and S[i].isdigit():
    #             val = val * 10 + ord(S[i]) - ord('0')
    #             i += 1
    #
    #         node = TreeNode(val)
    #         if level == len(path):
    #             if path:  # 避免第一个 node 的尴尬
    #                 path[-1].left = node
    #         else:
    #             path = path[:level]  # path 存储的是结点，会不断改变，
    #             path[-1].right = node
    #         path.append(node)
    #
    #     return path[0]  # 但连接关系不会变

    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack, i = [], 0
        n = len(S)

        while i < n:
            level = 0
            while S[i] == '-':
                level += 1
                i += 1

            val = 0
            # 因为字符串是以数字结尾的，所以要有 i < n 的判断，比使用 S[i] != '-'，快了 10 ms。
            while i < n and S[i].isdigit():
                val = val * 10 + int(S[i])
                i += 1

            node = TreeNode(val)
            if not stack:
                stack.append(node)
                continue
            while len(stack) > level:
                stack.pop()

            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node

            stack.append(node)

        return stack[0]

