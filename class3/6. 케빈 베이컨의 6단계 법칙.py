import sys

node, line = map(int,sys.stdin.readline().split())
lines = []
graph = {}
for i in range(node):
    a, b = map(int,sys.stdin.readline().split())
    lines.append([a,b])

for i in range(1,node+1):
    tmp = []
    for j in lines:
        if i == j[0]:
            tmp.append(j[1])
        elif i == j[1]:
            tmp.append(j[0])
    if tmp:
        graph[i] =  sorted(tmp)

ans = {}
for i in range(1,node+1):
    ans[i] = len(graph[i])

print(max(ans.values()))