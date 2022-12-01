import sys

for _ in range(int(sys.stdin.readline())):
    a = 0
    b = 1
    ans = 0
    tmp = int(sys.stdin.readline())

    if tmp == 0:
        pass
    else:
        for _ in range(tmp-1):
            ans = a + b
            a = b
            b = ans
    if tmp == 0:
        print(b,a)
    else:
        print(a,b)