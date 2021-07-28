from functools import wraps


def singleton(cls):
    instance = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance


@singleton
class MyClass:
    pass


a = MyClass()
b = MyClass()
print(id(a) == id(b))

