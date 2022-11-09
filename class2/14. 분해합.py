import sys

n = int(sys.stdin.readline())

m = len(list(map(int,str(n))))*9

if m > n:
    mn = 1
else:    
    mn = n - m

mx = n

for i in range(mn,mx+1):
    if n == sum(map(int,str(i))) + i:
        print(i)
        break
else:
    print(0)