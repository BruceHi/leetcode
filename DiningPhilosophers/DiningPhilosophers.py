# 哲学家进餐
import threading
from typing import Callable


def pickLeftFork():
    print('拿起左边叉子')
    return 1


def pickRightFork():
    print('拿起右边叉子')


def eat():
    print('吃')
    return 4


def putLeftFork():
    print('放下左边叉子')


def putRightFork():
    print('放下左边叉子')


class DiningPhilosophers:

    # 方法一、一个一个来。尽管测试时，输出与预期结果不符，但最终还是通过了。
    def __init__(self):
        self.lock = threading.Lock()

    # call the functions directly to execute, for example, eat()
    # def wantsToEat(self,
    #                philosopher: int,
    #                pickLeftFork: Callable[[], None],
    #                pickRightFork: Callable[[], None],
    #                eat: Callable[[], None],
    #                putLeftFork: Callable[[], None],
    #                putRightFork: Callable[[], None]) -> None:
    #     self.lock.acquire()
    #     pickLeftFork()
    #     pickRightFork()
    #     eat()
    #     putLeftFork()
    #     putRightFork()
    #     self.lock.release()

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self, philosopher, *actions):
        self.lock.acquire()
        print(actions)  # action 是元组的打包。
        # (<function pickLeftFork at 0x0000021DFB0F7048>, <function pickRightFork at 0x0000021DFB457598>,
        # <function eat at 0x0000021DFB4E5268>, <function putLeftFork at 0x0000021DFC588158>,
        # <function putRightFork at 0x0000021DFE5CF488>)

        b = map(lambda func: func(), actions)
        print(b)
        for i in b:
            print(i)  # 打印所有的结果，包括运行函数的返回值 None。还有其中的打印语句。

        list(map(lambda func: func(), actions))  # 使用 list 提取运行函数的结果，不打印返回值，只显示其中的 print 语句。
        # list(map(lambda func: func(), actions) 结果是 [1, None, 4, None, None]。因为没有调用 print 语句。
        # 所以只调用运行每个函数内部的 print 语句。

        # print([*map(lambda func: func(), actions)])
        print(list(map(lambda func: func(), actions)))  # 两个语句完全相同，更推荐下面的
        # 拿起左边叉子
        # 拿起右边叉子
        # 吃
        # 放下左边叉子
        # 放下左边叉子
        # [1, None, 4, None, None]

        a = list(map(lambda func: func(), actions))  # a 的真正结果是 [1, None, 4, None, None]
        a = a * 2
        print(a)

        self.lock.release()


if __name__ == '__main__':
    d = DiningPhilosophers()
    d.wantsToEat(0, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork)

    # Callable[[int], str] is a function of (int) -> str
    # 参数列表，返回类型 两个字段必不可少。
    # Callable[[], None] 代表该函数没有参数，没有返回值。
