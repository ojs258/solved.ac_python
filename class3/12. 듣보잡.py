import sys
from collections import Counter
n, m = map(int, sys.stdin.readline().split())
dname=[]; bname=[]
for i in range(n):
    dname.append(str(sys.stdin.readline().rstrip('\n')))
for i in range(m):
    bname.append(str(sys.stdin.readline().rstrip('\n')))

ans = sorted(set(dname) & set(bname))
print(len(ans))
for i in ans:
    print(i)