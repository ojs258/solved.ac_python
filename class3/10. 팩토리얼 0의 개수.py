import sys
from math import factorial
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())


tmp1 = factorial(n)
ans = 0

tmp2 = list(str(tmp1))
tmp2.reverse()
for i in tmp2:
    if i != '0':
        break
    ans += 1

if n == 0:
    print(1)
else:
    print(ans)