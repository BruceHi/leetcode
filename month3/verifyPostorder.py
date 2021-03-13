# 剑指 offer 33.二叉搜索树的后序遍历序列
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        def dfs(left, right):
            if left >= right:
                return True
            root = postorder[right]
            mid = left
            while postorder[mid] < root:
                mid += 1

            # 判断后面的是否都比root大
            for i in range(mid+1, right):
                if postorder[i] <= root:
                    return False

            return dfs(left, mid-1) and dfs(mid, right-1)

        return dfs(0, len(postorder)-1)
