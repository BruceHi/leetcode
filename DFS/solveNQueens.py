# N 皇后
from typing import List


class Solution:

    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     res = []
    #
    #     def DFS(queens, xy_diff, xy_sum):  # 捺（反斜杠），撇（斜杠）
    #         p = len(queens)
    #         if n == p:  # 只有在此结束时，才将结果 queens 添加至记录。
    #             res.append(queens)
    #             return
    #
    #         # 若是执行到循环结束（跳出循环）结束函数，则不添加到 res 。
    #         # 返回上层数据后，如 queens [1, 2, 3]会变为 [1, 2] 下次循环时 循环 3 的下一个元素。
    #
    #         for q in range(n):  # 列循环，记录列坐标。p 相当于是横坐标，加入了一个数据，横坐标自然加一。
    #             if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
    #                 DFS(queens+[q], xy_diff+[p-q], xy_sum+[p+q])  # 此时用 ‘+’ 是产生一个新对象，用过销毁
    #                 # DFS(queens.append(q), xy_diff.append(p-q), xy_sum.append(p+q))
    #
    #     DFS([], [], [])
    #     return [['.'*i + 'Q' + '.'*(n-1-i) for i in tmp] for tmp in res]

    # 使用 append 后面要用 remove，有一种归去来兮的感觉
    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     res = []
    #
    #     def DFS(queens, xy_diff, xy_sum):
    #         p = len(queens)
    #         if n == p:
    #             res.append(queens)
    #             return
    #
    #         for q in range(n):
    #             if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
    #                 xy_diff.append((p - q)), xy_sum.append((p + q))
    #                 DFS(queens+[q], xy_diff, xy_sum)  # 最好使用拼接字符串
    #                 xy_diff.remove(p-q), xy_sum.remove(p+q)  # 调用结束，恢复到上个状态
    #
    #
    #     DFS([], [], [])
    #     return [['.'*i + 'Q' + '.'*(n-1-i) for i in sol] for sol in res]

    # 使用集合试试
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def DFS(queens, xy_diff, xy_sum):
            p = len(queens)

            if n == p:
                res.append(queens)
                return

            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    DFS(queens+[q], xy_diff | {p-q}, xy_sum | {p+q})  # 集合并集相当于列表 + 。

        DFS([], set(), set())
        return [['.'*i + 'Q' + '.'*(n-1-i) for i in tmp] for tmp in res]

    # 问题二，有多少种解法
    # def totalNQueens(self, n: int) -> int:
    #
    #     # res = []
    #     res = 0
    #
    #     def DFS(queens, xy_diff, xy_sum):  # 捺（反斜杠），撇（斜杠）
    #         p = len(queens)
    #         if n == p:  # 只有在此结束时，才将结果 queens 添加至记录。
    #             # res.append(queens)
    #             nonlocal res  # 容器不需要如此写
    #             res += 1
    #             return
    #
    #         for q in range(n):  # 列循环，记录列坐标。p 相当于是横坐标，加入了一个数据，横坐标自然加一。
    #             if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
    #                 DFS(queens+[q], xy_diff+[p-q], xy_sum+[p+q])
    #
    #     DFS([], [], [])
    #     return res

    # 使用位运算
    # def totalNQueens(self, n: int) -> int:
    #
    #     count = 0
    #
    #     def DFS(row, col, pie, na):
    #         if row == n:
    #             nonlocal count
    #             count += 1
    #             return
    #
    #         # 与号前面部分是让 1 的位置是变成可以放 Q 的。后面部分是为了让 32 位左边部分的全部变成 0.
    #         # 结果：得到当前所有空位
    #         bits = ~ (col | pie | na) & (1 << n) - 1
    #         # 相当于从右到左开始循环
    #         while bits:
    #             p = bits & -bits  # 得到最低位的 1
    #             DFS(row+1, col | p, (pie | p) << 1, (na | p) >> 1)  # 也是生产新对象，结束调用销毁。
    #             bits &= bits - 1  # 抹掉最低位的 1
    #
    #     DFS(0, 0, 0, 0)
    #     return count
    #

# s = Solution()
# n = 4
# print(s.solveNQueens(n))


    # def totalNQueens(self, n: int) -> int:
    #     count = 0
    #
    #     def dfs(x, col, xy_sum, xy_diff):
    #         if len(col) == n:
    #             nonlocal count
    #             count += 1
    #             return
    #         i = x + 1
    #         for j in range(n):
    #             if j not in col and i + j not in xy_sum and i - j not in xy_diff:
    #                 dfs(i, col + [j], xy_sum + [i+j], xy_diff + [i-j])
    #
    #     for y in range(n):
    #         dfs(0, [y], [y], [-y])
    #     return count


    def totalNQueens(self, n: int) -> int:
        res = 0

        def dfs(queens, xy_sum, xy_diff):
            p = len(queens)
            if p == n:
                nonlocal res
                res += 1
                return
            for q in range(n):
                if q not in queens and p + q not in xy_sum and p - q not in xy_diff:
                    dfs(queens + [q], xy_sum + [p+q], xy_diff + [p-q])

        dfs([], [], [])
        return res


s = Solution()
n = 4
print(s.totalNQueens(n))
