#https://www.acmicpc.net/problem/11651

import sys

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    b, c = map(int, sys.stdin.readline().split())
    a.append((b,c))
a.sort(key=lambda x: (x[1], x[0]))
for i in a:
    print(i[0], i[1])