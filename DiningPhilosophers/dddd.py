# 参考网上
import random
import threading
from time import sleep

philosopher_num = fork_num = 5


class Fork:
    def __init__(self, index):
        self.index = index
        self._lock = threading.Lock()

    def pike_up(self):
        self._lock.acquire()

    def put_down(self):
        self._lock.release()


class Waiter:
    def __init__(self):
        self.forks = [Fork(idx) for idx in range(fork_num)]
        self.forks_using = [False] * fork_num

    def serve(self, philosopher):
        if not self.forks_using[philosopher.left_fork.index] and not self.forks_using[philosopher.right_fork.index]:
            self.forks_using[philosopher.left_fork.index] = True
            self.forks_using[philosopher.right_fork.index] = True
            self.forks[philosopher.left_fork.index].pike_up()
            self.forks[philosopher.right_fork.index].pike_up()
            return True
        else:
            return False

    def clean(self, philosopher):
        self.forks[philosopher.left_fork.index].put_down()
        self.forks[philosopher.right_fork.index].put_down()
        self.forks_using[philosopher.left_fork.index] = False
        self.forks_using[philosopher.right_fork.index] = False


class Philosopher(threading.Thread):
    def __init__(self, index, ):
        super().__init__()
        self.index = index
        self.left_fork = forks[self.index]
        self.right_fork = forks[(self.index + 1) % fork_num]

    def run(self):
        current_time = 0
        while current_time < 5:
            if waiter.serve(self):
                self.dining()
                waiter.clean(self)
                current_time += 1
            self.thinking()

    def dining(self):
        print(f"Philosopher {self.index} starts to eat.")
        sleep(random.uniform(1, 3) / 1000)
        print(f"Philosopher {self.index} finishes eating and leaves to think.")

    def thinking(self):
        sleep(random.uniform(1, 3) / 1000)


if __name__ == '__main__':
    waiter = Waiter()
    forks = [Fork(idx) for idx in range(fork_num)]
    philosophers = [Philosopher(idx) for idx in range(philosopher_num)]

    for philosopher in philosophers:
        philosopher.start()