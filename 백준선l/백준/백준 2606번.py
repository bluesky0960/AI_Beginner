def DFS(route):
    log = []
    store = [1]
    while store:
        start = store.pop()
        if start not in log:
            log.append(start)
            if start in route:
                tmp = list(set(route[start]) - set(log))
                store += tmp
    return len(log) - 1

point = int(input())
line = int(input())

route = {}

for i in range(line):
    point1, point2 = map(int, input().split())
    if point1 not in route:
        route[point1] = [point2]
    else:
        route[point1].append(point2)

    if point2 not in route:
        route[point2] = [point1]
    else:
        route[point2].append(point1)

print(DFS(route))