# 剑指offer 26.树的子结构
# 约定空树不是任意一个树的子结构
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 错误，
    # def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
    #     # 空树是相同的，这是判断两个树一模一样的，而不是判断子结构，[10,12,6,8,3,11]，[10,12,6,8]
    #     def is_same(A, B):
    #         if not A and not B:
    #             return True
    #         if not A or not B:
    #             return False
    #         return A.val == B.val and is_same(A.left, B.left) and is_same(A.right, B.right)
    #
    #     # bool(A and B) 表明若一个为空，则没有相同的子结构
    #     return bool(A and B) and (is_same(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

    # def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
    #     # A 是否包含 B(B 可以是空树),要从A的根就开始包含
    #     def recur(A, B):
    #         if not B:  # B 递归完了，就说明包含了。
    #             return True
    #         if not A or A.val != B.val:
    #             return False
    #         return recur(A.left, B.left) and recur(A.right, B.right)
    #
    #
    #     # # 直接这样写，会有 短路现象，直接输出 none，而不是false
    #     # return B and A and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
    #
    #     return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        if not A or not B:
            return False
        return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)




