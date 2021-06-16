class Singleton:
    __instance = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


a = Singleton()
b = Singleton()
print(id(a) == id(b))


def retry(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        times = 3
        if not res:
            for i in range(times):
                print(f'第{i+1}次重试！')
                res = func(*args, **kwargs)
                if not res:
                    break
    return inner





