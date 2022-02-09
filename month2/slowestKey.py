# 1629. 按键持续时间最长的键
from typing import List
from collections import defaultdict


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        dic = defaultdict(int)
        keysPressed = list(keysPressed)
        for i, (c, t) in enumerate(zip(keysPressed, releaseTimes)):
            if i == 0:
                dic[c] = t
            else:
                dic[c] = max(dic[c], t-releaseTimes[i-1])
        return sorted(dic, key=(lambda x: (dic[x], x)), reverse=True)[0]


s = Solution()
releaseTimes = [9,29,49,50]
keysPressed = "cbcd"
print(s.slowestKey(releaseTimes, keysPressed))

releaseTimes = [12,23,36,46,62]
keysPressed = "spuda"
print(s.slowestKey(releaseTimes, keysPressed))
