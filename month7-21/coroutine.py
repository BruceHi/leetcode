# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print(f'消费者：消费{n}')
#         r = '200 OK'
#
#
# def produce(c):
#     c.send(None)
#     for i in range(1, 5):
#         print(f'生产者：生产{i}')
#         r = c.send(i)
#         print(f'消费者：返回{r}')
#     c.close()
#
#
# c = consumer()
# produce(c)

def consumer():
    r = ''
    print('hello')
    while True:
        n = yield r
        if not n:
            return
        print(f'消费者：消费{n}')
        r = '200 OK'

# send进去的值在上一次yeild挂起的位置接收.
def produce(c):
    c.send(None)  # 这个命令开始执行生成器，从头开始执行，返回 r，然后结束
    for i in range(1, 5):
        print(f'生产者：生产{i}')
        r = c.send(i)  # 将 i 赋值到 n，即执行 n = ,然后执行下一句，直到再返回 r
        print(f'消费者：返回{r}')
    c.close()  # 生成器注销


c = consumer()  # 定义生成器
print('hhhh')
produce(c)


def generator():
    while True:
        receive = yield 1
        print('extra' + str(receive))


g = generator()
print(next(g))
print('j')
print(g.send(111))
print('d')
print(next(g))  # 相当于 g.send(None)，所以打印 extraNone，并循环执行 返回 1。
