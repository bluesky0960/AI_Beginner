import sys
from collections import deque

loop = int(sys.stdin.readline().rstrip())

for i in range(loop):
    
    order = deque(list(sys.stdin.readline().rstrip()))
    size = int(sys.stdin.readline().rstrip())
    tmp = sys.stdin.readline().rstrip()

    que = deque(tmp[1:-1].split(','))
    cnt = 0
    check = False
    if size == 0:
        que = deque()

    for k in range(len(order)):
        if order[k] == 'R':
            cnt += 1
        elif order[k] == 'D':
            if not que:
                print('error')
                check = True
                break
            if cnt % 2 != 0:
                que.pop()    
            else:
                que.popleft()
    if check == True:
        continue
    if cnt % 2 != 0:
        que.reverse()

    print('[' + ",".join(que) + ']')
