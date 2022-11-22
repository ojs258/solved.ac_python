import sys
que = []
for _ in range(int(sys.stdin.readline())):
    a = list(sys.stdin.readline().split())

    if a[0] == 'push_front':
        que.insert(len(que),a[1])
    elif a[0] == 'push_back':
        que.insert(0,a[1])
    elif a[0] == 'pop_front':
        if len(que) != 0:
            print(que.pop())
        else:
            print(-1)
    elif a[0] == 'pop_back':
        if len(que) != 0:
            print(que.pop(0))
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(que))
    elif a[0] == 'empty':
        if len(que) != 0:
            print(0)
        else:
            print(1)
    elif a[0] == 'back':
        if len(que) != 0:
            print(que[0])
        else:
            print(-1)
    elif a[0] == 'front':
        if len(que) != 0:
            print(que[-1])
        else:
            print(-1)