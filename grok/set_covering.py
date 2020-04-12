states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
stations = {'kone': {'id', 'nv', 'ut'},
            'ktwo': {'wa', 'id', 'mt'},
            'kthree': {'or', 'nv', 'ca'},
            'kfour': {'nv', 'ut'},
            'kfive': {'ca', 'az'}}
final_station = set()

# 每次循环都找到覆盖州最多的广播站，并将州减去。形成新的未覆盖的州。
while states_needed:  # 开始循环，要清空临时变量
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        # 有了这个，以前曾经覆盖过的，就是空集了。
        covered = states_needed & states  # 必须要有这个，否则遍历到的永远是第一次便利到的。
        if len(covered) > len(states_covered):  # 此次覆盖的与上次覆盖的多少比较
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_station.add(best_station)

print(final_station)
