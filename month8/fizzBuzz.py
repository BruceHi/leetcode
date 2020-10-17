# Fizz Buzz
from typing import List


class Solution:
    # def fizzBuzz(self, n: int) -> List[str]:
    #     res = []
    #     for i in range(1, n+1):
    #         if not i % 3 and not i % 5:
    #             res.append('FizzBuzz')
    #         elif not i % 3:
    #             res.append('Fizz')
    #         elif not i % 5:
    #             res.append('Buzz')
    #         else:
    #             res.append(str(i))
    #     return res

    # def fizzBuzz(self, n: int) -> List[str]:
    #     res = [str(i+1) for i in range(n)]
    #     for i in range(1, n+1):
    #         if not i % 3 and not i % 5:
    #             res[i-1] = 'FizzBuzz'
    #         elif not i % 3:
    #             res[i-1] = 'Fizz'
    #         elif not i % 5:
    #             res[i-1] = 'Buzz'
    #     return res

    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if not i % 3 and not i % 5:
                res.append('FizzBuzz')
            elif not i % 3:
                res.append('Fizz')
            elif not i % 5:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res


s = Solution()
print(s.fizzBuzz(15))
