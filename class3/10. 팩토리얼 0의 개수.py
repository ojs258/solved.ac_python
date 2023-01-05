import sys

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1) 

n = int(sys.stdin.readline())
sys.setrecursionlimit(10**7)

tmp = fac(n)
ans = 0
while tmp % 10 == 0:
    if tmp == 0:
        print(1)
    tmp //= 10
    ans += 1
print(ans)