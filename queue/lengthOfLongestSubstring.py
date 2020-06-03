# 无重复最长字串长度（滑动窗口）
from collections import deque


class Solution:

    # # 双端队列，找的其实是某一元素为结尾的无重复字串
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     queue = deque()
    #     count, res = 0, 0
    #     for c in s:
    #         if c in queue:
    #             count -= 1
    #             while queue.popleft() != c:
    #                 count -= 1
    #         # while c in queue:  # 这样每次删完一个，都要遍历整个 queue 来找到 c，不如上面的快。
    #         #     queue.popleft()
    #         #     count -= 1
    #         queue.append(c)
    #         count += 1
    #         res = max(count, res)
    #     return res

    # 使用 set 模拟上述过程
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     record = set()
    #     res, left, count = 0, 0, 0
    #     for c in s:
    #         while c in record:
    #             record.remove(s[left])
    #             left += 1
    #             count -= 1
    #         record.add(c)
    #         count += 1
    #         res = max(count, res)
    #     return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        res, left = 0, 0
        for i, c in enumerate(s):
            if c in hash_map:
                left = max(hash_map[c], left)
            hash_map[c] = i + 1
            res = max(res, i-left+1)
        return res


s = Solution()

# ...a...b....a...a....b... 举例应该是这样的例子吧，第二个a会把start更新到第一个a之后，
# 第三个a会把start更新到第二个a之后，此时start=Idx(a2]+1,到第二个b会选择max[map(b),start]=start
string = "abaaaab"  # left 为什么要定义 max，这里可以解释遍历到最后一个 a,left 是全局的，然而 map(b)还是 2，
print(s.lengthOfLongestSubstring(string))

string = "abcbcbb"
print(s.lengthOfLongestSubstring(string))

string = "bbbbb"
print(s.lengthOfLongestSubstring(string))

string = "pwwkew"
print(s.lengthOfLongestSubstring(string))
