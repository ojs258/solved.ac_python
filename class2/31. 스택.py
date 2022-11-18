import sys
stk = []
for _ in range(int(sys.stdin.readline())):
    a = list(sys.stdin.readline().split())

    if a[0] == 'push':
        stk.append(a[1])
    elif a[0] == 'pop':
        if len(stk) != 0:
            print(stk.pop())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(stk))
    elif a[0] == 'empty':
        if len(stk) != 0:
            print(0)
        else:
            print(1)
    else:
        if len(stk) != 0:
            print(stk[-1])
        else:
            print(-1)