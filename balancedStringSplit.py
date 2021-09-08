# 1221. 分割平衡字符串
class Solution:
    # 平衡字符串的特点是可以分割为两个平衡字符串（1->2)，然后再分割
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        left = 0
        for c in s:
            if c == "L":
                left += 1
            else:
                left -= 1
            if left == 0:
                res += 1
        return res




obj = Solution()
s = "RLRRLLRLRL"
print(obj.balancedStringSplit(s))

s = "RLLLLRRRLR"
print(obj.balancedStringSplit(s))

s = "LLLLRRRR"
print(obj.balancedStringSplit(s))

s = "RLRRRLLRLL"
print(obj.balancedStringSplit(s))

s = "LRLLLRRLLRRRLLLRRR"
print(obj.balancedStringSplit(s))
