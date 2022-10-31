import sys

k, n = map(int,sys.stdin.readline().split())

tmp = []
for i in range(k):
    tmp.append(int(sys.stdin.readline()))

for i in range(k):
    print(round(tmp[i] / (sum(tmp) // n))) 