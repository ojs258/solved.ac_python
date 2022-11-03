import sys

for _ in range(int(sys.stdin.readline())):
    cnt = 1
    n, m = map(int,sys.stdin.readline().split())
    imp = list(map(int,sys.stdin.readline().split()))
    idx = list(range(0,n))

    idx[m] = 'fdoc' # need to (f)ind (doc)umentation

    while True:
        if max(imp) == imp[0]:
            if idx[0] == 'fdoc':
                print(cnt)
                break
            imp.pop(0)
            idx.pop(0)
            cnt += 1
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
