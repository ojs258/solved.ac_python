import sys

asc = [i for i in range(1, 9)]

num = [int(sys.stdin.readline())
for _ in range(int(sys.stdin.readline()))]

for i in range(len(num)):
    for j in range(len(asc)):
        num[i] == asc[j]