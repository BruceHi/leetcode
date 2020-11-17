# 哲学家进餐
import threading
from threading import Condition, Semaphore
from collections import defaultdict

# 方法一：一个吃完一个来
# class DiningPhilosophers:
#     def __init__(self):
#         self.lock = threading.Lock()
#
#     # call the functions directly to execute, for example, eat()
#     def wantsToEat(self,
#                    philosopher: int,
#                    *actions) -> None:
#         self.lock.acquire()
#         list(map(lambda func: func(), actions))
#         self.lock.release()

# # 方法二、使用条件变量
# class DiningPhilosophers:
#
#     def __init__(self):
#         self.cond = Condition()
#         self.dic = defaultdict(bool)
#
#     # call the functions directly to execute, for example, eat()
#     def wantsToEat(self,
#                    philosopher: int,
#                    *actions) -> None:
#         l_neighbor, r_neighbor = (philosopher-1) % 5, (philosopher+1) % 5
#
#         with self.cond:
#             self.cond.wait_for(lambda: not self.dic[l_neighbor] and not self.dic[r_neighbor])
#             self.dic[philosopher] = True
#
#         list(map(lambda func: func(), actions))
#
#         with self.cond:
#             self.dic[philosopher] = False
#             self.cond.notify_all()

# 方法三、使用信号量
# 国际站 https://leetcode.com/problems/the-dining-philosophers/discuss/746300/Python-Semaphores-or-Cycle-Breaking
class DiningPhilosophers:
    def __init__(self):
        self.forks = [Semaphore() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   *actions) -> None:
        a, b = self.forks[philosopher], self.forks[(philosopher+1)%5]
        with a:
            with b:
                list(map(lambda func: func(), actions))
