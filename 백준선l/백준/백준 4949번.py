import sys
while True:
    a = sys.stdin.readline().rstrip()
    log = []
    
    if a == '.':
        break

#Half Moon tonight (At least it is better than no Moon at all].

    for ch in a:
        if ch == '(' or ch == '[':
            log.append(ch)
        elif ch == ')':
            if log and log[-1] == '(':
                log.pop()
            else:
                print('no')
                break
        elif ch == ']':
            if log and log[-1] == '[':
                log.pop()
            else:
                print('no')
                break
    else:
        print('yes')

# "yes" if true_flag and not(stack) else "no"
