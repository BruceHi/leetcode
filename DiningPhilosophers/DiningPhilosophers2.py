# 哲学家进餐
import threading
from typing import Callable
from collections import deque, defaultdict
from threading import Condition, Thread
from concurrent.futures import ThreadPoolExecutor
import time
import random


def pickLeftFork(i):

    print(f'{i}拿起左边叉子')
    time.sleep(0.2)


def pickRightFork(i):

    print(f'{i}拿起右边叉子')
    time.sleep(0.2)


def eat(i):

    print(f'{i}吃')
    time.sleep(1)


def putLeftFork(i):

    print(f'{i}放下左边叉子')
    time.sleep(0.2)

def putRightFork(i):

    print(f'{i}放下左边叉子')
    time.sleep(0.2)

# https://leetcode-cn.com/problems/the-dining-philosophers/solution/pythonliang-chong-jie-fa-by-yuhan-huang/
class DiningPhilosophers:

    # def __init__(self):
    #     self.queue = deque()
    #
    # def wantsToEat(self, philosopher, *actions):
    #     self.queue.extend(actions)
    #     # 后面写什么都没有关系，只是可迭代的长度必须要 等于 len(queue) 的长度，才能迭代完全。
    #     # print(list(map(lambda _: self.queue.popleft(), range(len(actions)))))
    #     # 结果
    #     # [<function pickLeftFork at 0x0000024E3FC67048>, <function pickRightFork at 0x0000024E3FFC7598>,
    #     # <function eat at 0x0000024E40055268>, <function putLeftFork at 0x0000024E410F8158>,
    #     # <function putRightFork at 0x0000024E4410F488>]
    #
    #     list(map(lambda _: self.queue.popleft()(), actions))

    def __init__(self):
        self.cond = Condition()
        self.dic = defaultdict(bool)

    def wantsToEat(self, philosopher: int, *actions) -> None:
        l_neighbor = philosopher - 1 if philosopher > 0 else 4
        r_neighbor = philosopher + 1 if philosopher < 4 else 0

        with self.cond:
            self.cond.wait_for(lambda: not self.dic[l_neighbor] and not self.dic[r_neighbor])
            self.dic[philosopher] = True  # 修改变量最后放在条件事件锁中，防止其他进行修改。
            # self.cond.notify_all() 这个没作用
            # print(philosopher)
        # 注意不能直接给 leetcode 使用，使用时 func(philosopher) 下面要没有参数的。
        list(map(lambda func: func(philosopher), actions))  # 一系列事件都是整体的，这样不太好，看起来就像一个一个来的。

        # self.dic[philosopher] = False
        with self.cond:
            self.dic[philosopher] = False  # 该事件结束，就可以通知其他事件了。若满足继续执行下去。否则死锁。
            self.cond.notify_all()


if __name__ == '__main__':
    d = DiningPhilosophers()
    threads = []
    for i in range(5):
        t = Thread(target=d.wantsToEat, args=(i, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
        t.start()
        threads.append(t)
        # d.wantsToEat(i, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork)
    #
    # for t in threads:
    #     t.join()
