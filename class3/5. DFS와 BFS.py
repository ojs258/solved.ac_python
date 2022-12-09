import sys
from collections import deque

def bfs(graph,root):
    visit = []
    que = deque([root])

    while que:
        n = que.popleft()
        if n not in visit:
            visit.append(n)
            que += graph[n]-set(visit)
    return visit

def dfs(graph,root):
    visit = []
    stk = [root]

    while stk:
        n = stk.pop()
        if n not in visit:
            visit.append(n)
            stk += graph[n]-set(visit)
    return visit        

n, m, v = map(int,sys.stdin.readline().split())
tmp = []
graph = {}
cnt = 0
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    tmp.append([a,b])

cond = len(tmp)
while cnt < cond-1:
    if tmp[cnt][0] == tmp[cnt+1][0]:
        tmp[cnt].append(tmp[cnt+1][1])
        tmp.remove(tmp[cnt+1])
    else:
        cnt += 1
    cond = len(tmp)
for i in tmp:
    graph[i[0]] = set(list(i[1:]))

print(dfs(graph,v), dfs(graph,v), sep='\n')
