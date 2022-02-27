# 참고내용 : https://hooongs.tistory.com/329 접근 방식만 참고
import sys
size = int(sys.stdin.readline().rstrip())

num = list(map(int, sys.stdin.readline().split()))

stack = [[0 for i in range(2)] for j in range(1)]
oken = [-1] * size # 오큰수 배열

stack[0][0] = num[0] 
stack[0][1] = 0

for i in range(1, size):
    try: # 스택에 아무것도 없을 때,
        while stack[-1][0] < num[i]: 
            a, b = stack.pop()
            oken[b] = num[i]

    except IndexError:
        pass
    stack.append([num[i],i])

for i in oken:
    print(i, end = ' ')


'''  # 시간 초과 발생 n * 2
for i in range(size):
    if i == size - 1:
        print(-1, end = ' ')
        break
    for j in range(i+1, size):
        if stack[i] < stack[j]:
            print(stack[j], end = " ")
            stack[i] = 0
            break
        
        if stack[i] == max(stack):
            print(-1, end = ' ')
            break
'''