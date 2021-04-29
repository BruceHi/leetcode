# 6. z 字形变换
class Solution:

    # https://leetcode-cn.com/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/
    # 模拟行索引的变化
    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows < 2:
    #         return s
    #     res = [''] * numRows
    #     i, flag = 0, -1
    #     for c in s:
    #         res[i] += c
    #         if i == 0 or i == numRows - 1:
    #             flag = -flag
    #         i += flag
    #     return ''.join(res)

    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows < 2:
    #         return s
    #     res = [''] * numRows
    #     i, flag = 0, -1
    #     for c in s:
    #         res[i] += c
    #         if i == 0 or i == numRows-1:
    #             flag = -flag
    #         i += flag
    #     return ''.join(res)

    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = [''] * numRows
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows-1:
                flag = -flag
            i += flag
        return ''.join(res)



obj = Solution()
s = "LEETCODE"
numRows = 3
print(obj.convert(s, numRows))

s = "LEETCODEISHIRING"
numRows = 3
print(obj.convert(s, numRows))

s = "LEETCODEISHIRING"
numRows = 4
print(obj.convert(s, numRows))
