import sys

n, x = map(int,sys.stdin.readline().split())
ex = list(map(int,sys.stdin.readline().split()))

for i in ex:
    if i < x:
        print(i, end=' ')