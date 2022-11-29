from collections import Counter
import sys

n, m, b = map(int,sys.stdin.readline().split())

dirt = []
for i in range(n):
        for j in map(int,sys.stdin.readline().split()):
            dirt.append(j)

height, time = 0, sys.maxsize

min_h = min(dirt)
max_h = max(dirt)
hap = sum(dirt)
dirt = dict(Counter(dirt))

for i in range(min_h, max_h+1):
    if hap + b >= i * n * m:
        ctime = 0
        for key in dirt:
            if key > i:
                ctime += (key - i) * dirt[key] * 2
            else:
                ctime += (i - key) * dirt[key]
        
        if ctime <= time:
            time = ctime
            height = i

print(time, height)