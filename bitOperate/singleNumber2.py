# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
from typing import List
from collections import Counter


class Solution:
    # 词频
    # def singleNumber(self, nums):
    #     count = Counter(nums)
    #     # res = []
    #     # for key in count:
    #     #     if count[key] == 1:
    #     #         res.append(key)  # res += [key]
    #     #         if len(res) == 2:
    #     #             break
    #     # return res
    #     return [x for x in count if count[x] == 1]

    # 词频
    # def singleNumber(self, nums: List[int]) -> List[int]:
    #     count = Counter(nums)
    #     return [x for x in count if count[x] == 1]

    # 设题目中这两个只出现1次的数字分别为A和B，如果能将A，B分开到二个数组中，那显然符合“异或”解法的关键点了。
    # 因此这个题目的关键点就是将A，B分开到二个数组中。由于A，B肯定是不相等的，因此在二进制上必定有一位是不同的。
    # 根据这一位是0还是1可以将A，B分开到A组和B组。而这个数组中其它数字要么就属于A组，要么就属于B组。
    # 再对A组和B组分别执行“异或”解法就可以得到A，B了。而要判断A，B在哪一位上不相同，只要根据A异或B的结果就可以知道了，
    # 这个结果在二进制上为1的位就说明A，B在这一位上是不相同的。
    # 作者：BugFreezrr
    # 链接：https://leetcode-cn.com/problems/single-number-iii/solution/java-yi-huo-100-yao-shi-kan-bu-dong-wo-jiu-qu-chu-/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 位运算
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num

        diff = bitmask & -bitmask
        x = 0
        for num in nums:
            if num & diff:
                x ^= num
        return [x, x ^ bitmask]



s = Solution()
a = [1,2,1,3,2,5]
print(s.singleNumber(a))
