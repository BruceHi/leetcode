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
    while True:
        n = yield r
        if not n:
            return
        print(f'消费者：消费{n}')
        r = '200 OK'


def produce(c):
    c.send(None)
    for i in range(1, 5):
        print(f'生产者：生产{i}')
        r = c.send(i)
        print(f'消费者：返回{r}')
    c.close()


c = consumer()
produce(c)
