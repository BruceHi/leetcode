# 667. 键值映射

# 1. 普通方法
class MapSum:

    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        # res = 0
        # for k, v in self.map.items():
        #     if k.startswith(prefix):
        #         res += v
        # return res
        return sum(v for k, v in self.map.items() if k.startswith(prefix))

# 2.字典树方法没有看



m = MapSum()
m.insert('apple', 3)
print(m.sum('ap'))
m.insert('app', 2)
print(m.sum('ap'))
