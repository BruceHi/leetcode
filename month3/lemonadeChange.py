# 860. 柠檬水找零
from typing import List


class Solution:
    # def lemonadeChange(self, bills: List[int]) -> bool:
    #     count5, count10 = 0, 0
    #     for bill in bills:
    #         if bill == 5:
    #             count5 += 1
    #         elif bill == 10:
    #             if count5 == 0:
    #                 return False
    #             count5, count10 = count5-1, count10+1
    #         else:
    #             if count5 == 0:
    #                 return False
    #             elif count5 <= 2 and count10 == 0:
    #                 return False
    #             elif count10 >= 1:
    #                 count5, count10 = count5-1, count10-1
    #             else:
    #                 count5 -= 3
    #     return True


    def lemonadeChange(self, bills: List[int]) -> bool:
        count5, count10 = 0, 0
        for bill in bills:
            if bill == 5:
                count5 += 1
            elif bill == 10:
                count5, count10 = count5-1, count10+1
            else:
                if count10:
                    count5, count10 = count5-1, count10-1
                else:
                    count5 -= 3
            if count5 < 0:
                return False
        return True


s = Solution()
bills = [5,5,5,10,20]
print(s.lemonadeChange(bills))

bills = [5,5,10]
print(s.lemonadeChange(bills))

bills = [10,10]
print(s.lemonadeChange(bills))

bills = [5,5,10,10,20]
print(s.lemonadeChange(bills))

bills = [5,5,5,10,5,5,10,20,20,20]
print(s.lemonadeChange(bills))
