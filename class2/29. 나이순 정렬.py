import sys

ans = []
for i in range(int(sys.stdin.readline())):
    y, n = map(str,sys.stdin.readline().split())
    ans.append([int(y), i, n])

ans = sorted(ans, key = lambda x: (x[0], x[1]))

for i in range(len(ans)):
    print(ans[i][0],ans[i][2])