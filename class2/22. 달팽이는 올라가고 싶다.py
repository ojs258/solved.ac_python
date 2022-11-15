import sys

a, b, v = map(int, sys.stdin.readline().split())

tmp1 = v - a
tmp2 = a - b
tmp3 = tmp1 // tmp2
tmp4 = tmp1 % tmp2

if tmp4 == 0:
    print(tmp3 + 1)
else:
    print(tmp3 + 2)