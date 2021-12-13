# 405. 数字转换为 16 进制数

class Solution:
    # 整数，部分负数
    # def toHex(self, num: int) -> str:
    #     # return hex(num)
    #     res = []
    #     while num != 0:
    #         res.append(num % 16)
    #         num //= 16
    #     # a = True if num > 0 else 3
    #     # true - value if cond else false - value
    #     return ''.join(reversed([str(x) if x < 10 else chr(ord('a') + x-10) for x in res]))

    # 因为只有32位， 而 0000-1111，表示 0-15之间的数，即 4 位表示一个，所以 16 进制最多有 8 个字符
    # def toHex(self, num: int) -> str:
    #     CONV = "0123456789abcdef"
    #     ans = []
    #     # 32位2进制数，转换成16进制 -> 4个一组，一共八组
    #     for _ in range(8):
    #         ans.append(num % 16)
    #         num //= 16
    #         if not num:
    #             break
    #     return "".join(CONV[n] for n in ans[::-1])

    def toHex(self, num: int) -> str:
        res = []
        for _ in range(8):
            res.append(num % 16)
            num //= 16
            if not num:
                break
        conv = '0123456789abcdef'  # 整数映射字符串的方法
        return ''.join([conv[i] for i in res][::-1])


s = Solution()
print(s.toHex(26))

print(s.toHex(-1))
