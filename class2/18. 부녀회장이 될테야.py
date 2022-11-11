import sys

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    peo = list(range(1,n+1))
    for _ in range(k):
        for i in range(1, n):
            peo[i] = peo[i] + peo[i-1]
    print(peo[-1])
