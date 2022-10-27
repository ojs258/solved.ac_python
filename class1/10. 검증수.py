import sys

tmp = 0
num = list(map(int,sys.stdin.readline().split()))

for i in num:
    tmp = tmp + pow(i,2)
print(tmp % 10)