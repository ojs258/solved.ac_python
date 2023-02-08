import sys
from collections import Counter
n, m = map(int, sys.stdin.readline().split())
name=[]
for i in range(n+m):
    name.append(str(sys.stdin.readline().rstrip('\n')))

ndict = dict(Counter(name))
print()