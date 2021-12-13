# 423. 从英文中重建数字
from collections import Counter


class Solution:
    # 草泥马，全错了
    # def originalDigits(self, s: str) -> str:
    #     word = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
    #             'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
    #             'nine': 9, 'zero': 0}
    #     n = len(s)
    #     res = []
    #
    #     def dfs(cur, idx, tmp):
    #         if len(tmp) > 5:
    #             return
    #
    #         if len(''.join(cur)) == n:
    #             res.append(cur)
    #             return
    #
    #         for i in range(n):
    #             if i not in idx:
    #                 new = tmp + s[i]
    #                 if new in word:
    #                     dfs(cur+[new], idx + [i], '')
    #                 else:
    #                     dfs(cur, idx+[i], new)
    #
    #     dfs([], [], '')
    #     return ''.join(sorted(str(word[key]) for key in res[0]))

    # def originalDigits(self, s: str) -> str:
    #     c = Counter(s)
    #
    #     cnt = [0] * 10
    #     cnt[0] = c["z"]
    #     cnt[2] = c["w"]
    #     cnt[4] = c["u"]
    #     cnt[6] = c["x"]
    #     cnt[8] = c["g"]
    #
    #     cnt[3] = c["h"] - cnt[8]
    #     cnt[5] = c["f"] - cnt[4]
    #     cnt[7] = c["s"] - cnt[6]
    #
    #     cnt[1] = c["o"] - cnt[0] - cnt[2] - cnt[4]
    #
    #     cnt[9] = c["i"] - cnt[5] - cnt[6] - cnt[8]
    #
    #     return "".join(str(x) * cnt[x] for x in range(10))

    # 因为有 nine 占有两个 n 所以不能有 count['n']
    # 同理，因为 three，所以不能有 count['e']
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        c = [0] * 10

        c[8] = count['g']
        c[4] = count['u']
        c[2] = count['w']
        c[6] = count['x']
        c[0] = count['z']

        c[3] = count['h'] - c[8]
        c[5] = count['f'] - c[4]
        c[7] = count['s'] - c[6]

        c[9] = count['i'] - c[5] - c[6] - c[8]
        c[1] = count['o'] - c[0] - c[2] - c[4]

        return ''.join(str(i) * x for i, x in enumerate(c) if x)

obj = Solution()
s = "owoztneoer"
print(obj.originalDigits(s))

s = "fviefuro"
print(obj.originalDigits(s))

s = "fivefour"
print(obj.originalDigits(s))

s = "twotow"
print(obj.originalDigits(s))

s = "egith"
print(obj.originalDigits(s))

s = "nnei"
print(obj.originalDigits(s))