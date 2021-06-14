from typing import List


class Solution:
    # 超时
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_sub(s, p):
            j = 0
            for c in s:
                if c == p[j]:
                    j += 1
                if j == len(p):
                    return True
            return False
        s = list(s)
        for i, num in enumerate(removable):
            s[num] = ''
            if not is_sub(s, p):
                return i
        return len(removable)


obj = Solution()
s = "abcacb"
p = "ab"
removable = [3,1,0]
print(obj.maximumRemovals(s, p, removable))

s = "abcbddddd"
p = "abcd"
removable = [3,2,1,4,5,6]
print(obj.maximumRemovals(s, p, removable))

s = "abcab"
p = "abc"
removable = [0,1,2,3,4]
print(obj.maximumRemovals(s, p, removable))

s = "qlevcvgzfpryiqlwy"
p = "qlecfqlw"
removable = [12,5]
print(obj.maximumRemovals(s, p, removable))
