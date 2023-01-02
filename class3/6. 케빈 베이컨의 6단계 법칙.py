import sys
from collections import deque

def bfs(start, graph, node):
    cnt = [0] * (node+1)
    visit=[start]
    que = deque([start])

    while que:
        n = que.popleft()
        for i in graph[n]:
            if i not in visit:
                cnt[i] = cnt[n] + 1
                visit.append(i)
                que.append(i)
    return sum(cnt)


node, line = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(node+1)]
lines = []

for i in range(line):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

tmp=[]
for i in range(1,node+1):
    tmp.append(bfs(i ,graph, node))
print(tmp.index(min(tmp))+1)