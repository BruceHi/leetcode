# 哲学家进餐
import threading
from typing import Callable
from collections import deque, defaultdict
from threading import Condition, Thread
from concurrent.futures import ThreadPoolExecutor
import time
import random


def pickLeftFork():
    print('拿起左边叉子')


def pickRightFork():
    print('拿起右边叉子')


def eat():
    time.sleep(random.choice([1, 2, 3, 4]))
    print('吃')


def putLeftFork():
    print('放下左边叉子')


def putRightFork():
    print('放下左边叉子')



class DiningPhilosophers:

    def __init__(self, philosopher=None):
        self.cond = Condition()
        self.dic = defaultdict(bool)
        self.i = philosopher

    def pickLeftFork(self):
        print(f'{self.i} 拿起左边叉子')
        return 1

    def pickRightFork(self):
        print(f'{self.i} 拿起右边叉子')

    def eat(self):
        print(f'{self.i} 吃')
        return 4

    def putLeftFork(self):
        print(f'{self.i}放下左边叉子')

    def putRightFork(self):
        print(f'{self.i}放下左边叉子')


    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: Callable[[], None],
                   pickRightFork: Callable[[], None],
                   eat: Callable[[], None],
                   putLeftFork: Callable[[], None],
                   putRightFork: Callable[[], None]) -> None:

        l_neighbor = philosopher - 1 if philosopher > 0 else 4
        r_neighbor = philosopher + 1 if philosopher < 4 else 0

        with self.cond:  # 条件事件
            self.cond.wait_for(lambda: not self.dic[l_neighbor] and not self.dic[r_neighbor])
            self.dic[philosopher] = True
            # print(philosopher)
            # list(map(lambda func: func(), actions))  # 一系列事件都是整体的，这样不太好，看起来就像一个一个来的。

        self.dic[philosopher] = False


if __name__ == '__main__':
    # d = DiningPhilosophers()
    # for i in range(5):
    #     t = Thread(target=d.wantsToEat, args=(i, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
    #     t.start()
        # d.wantsToEat(i, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork)

    for i in range(5):
        d = DiningPhilosophers(i)
        t = Thread(target=d.wantsToEat, args=(i, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
        t.start()



