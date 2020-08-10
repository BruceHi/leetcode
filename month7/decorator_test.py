# 闭包
def createCounter():
    n = 0

    def counter():
        nonlocal n
        n += 1
        return n
    return counter


# def createCounter():
#     n = [0]
#
#     def counter():
#         n[0] += 1
#         return n[0]
#     return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


# 正确
# def count():
#     def g(j):
#         def f():
#             return j * j
#         return f
#
#     fs = []
#     for i in range(1, 4):
#         fs.append(g(i))
#     return fs

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs

def count():
    fs = []
    for i in range(1, 4):
        def f(j=i):  # 使用默认参数
            return j * j
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


# 装饰器
import time, functools


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end-start))
        return res
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)


# 没有 @functools.wraps(fn) 时，下面结果是 wrapper
print(fast.__name__)
print(slow.__name__)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# 测试 begin call、end call
#
# def log(fun):
#     @functools.wraps(fun)
#     def wrapper(*args, **kwargs):
#         print('begin call ……')
#         fun(*args, **kwargs)
#         print('end call ……')
#     return wrapper
#
#
# @log
# def show():
#     print('haha')
#
#
# show()

#


def log(text):
    if isinstance(text, str):
        def decorator(fun):
            @functools.wraps(fun)
            def wrapper(*args, **kwargs):
                print('call', text)
                return fun(*args, **kwargs)
            return wrapper
        return decorator

    @functools.wraps(text)
    def wrapper(*args, **kwargs):
        print('call func')
        return text(*args, **kwargs)  # 函数名为 text
    return wrapper

# @log('execute')  # 相当于 test = log('execute')(test)
# def test(a):
#     return 2


# 相当于 test = log(test)


@log
def test(a):
    return 2


print(test.__name__)
print(test(2))

print(max(1, 2, 3))


from functools import partial
max2 = partial(max, 10)
b = [1, 2, 3]
print(max2(*b))


from functools import lru_cache


@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y


print(add(1, 2))
print(add(1, 2))
print(add(2, 3))


