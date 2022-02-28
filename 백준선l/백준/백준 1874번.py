loop = int(input())

stack = []
answer = []
suyeol = 1
check = 0

for i in range(loop):
    num = int(input())
    
    while suyeol <= num:
        answer.append('+')
        stack.append(suyeol)
        suyeol += 1
    
    if num == stack[-1]:
        answer.append('-')
        stack.pop()
    else:
        check = 1
        break

if check == 0:
    for i in answer:
        print(i)
else:
    print('NO')
