# 哲学家就餐问题
import threading
import time

# 保证能有相隔至少一个位置的哲学家能同时进餐
# 进餐的同时，加上锁
class DiningPhilosophy(object):
    def __init__(self):
        self.cond = threading.Condition()  # 锁
        self.forks = [{0, 7, 8}, {0, 8, 9}, {0, 9, 5}, {0, 5, 6}, {0, 6, 7}]  # 叉子
        self.t = 0  # 加锁条件

    def wants_to_eat(self, philosopher, *actions):
        """
        首先先让philosophy==0的线程激活，然后将t+哲学家编号+5，使得相隔至少一个座位的哲学家可以进餐
        然后开始执行拿起叉子——》就餐——》放下叉子的函数
        最后执行完毕的哲学家线程将t-(哲学家编号+5)，通知其他哲学家线程可以开始竞争进餐
        """
        with self.cond:
            self.cond.wait_for(lambda: self.t in self.forks[philosopher])
            self.t += philosopher + 5
            # self.cond.notify_all()
        [*map(lambda func: func(philosopher), actions)]
        with self.cond:
            self.t -= philosopher + 5
            self.cond.notify_all()

def pick_left_fork(philosopher):  # 拿起左边叉子
    output.append([philosopher, 1, 1])
    print(f'{philosopher}拿起左边叉子')
    print([philosopher, 1, 1])
    time.sleep(0.2)

def pick_right_fork(philosopher):  # 拿起右边叉子
    output.append([philosopher, 2, 1])
    print(f'{philosopher}拿起右边叉子')
    print([philosopher, 2, 1])
    time.sleep(0.2)

def eat(philosopher):  # 就餐
    output.append([philosopher, 0, 3])
    print(f'{philosopher}吃')
    print([philosopher, 0, 3])
    time.sleep(2)

def put_left_fork(philosopher):  # 放下左边叉子
    output.append([philosopher, 1, 2])
    print(f'{philosopher}放下左边叉子')
    print([philosopher, 1, 2])
    time.sleep(0.2)

def put_right_fork(philosopher):  # 放下右边叉子
    output.append([philosopher, 2, 2])
    print(f'{philosopher}放下右边叉子')
    print([philosopher, 2, 2])
    time.sleep(0.2)


output = []

if __name__ == "__main__":
    # 设置进餐的次数
    count = int(input("n = "))

    # 创建就餐线程
    p = DiningPhilosophy()
    while count:
        philo_threads = []
        for i in range(5):
            t = threading.Thread(target=p.wants_to_eat,
            args=(i,
            pick_left_fork,
            pick_right_fork,
            eat,
            put_left_fork,
            put_right_fork))
            t.start()
            philo_threads.append(t)

        # 阻塞主进程
        for t in philo_threads:
            t.join()

        count -= 1

    # 输出结果
    print(output)