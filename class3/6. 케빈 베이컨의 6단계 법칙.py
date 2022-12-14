import sys

def dfs(graph,start,point):
    cnt = 0
    visit=[]
    for i in point:
        stk=[start]
        while stk:
            n = stk.pop(0)
            if n not in visit:
                if i in graph[n]:
                    cnt =+ 1
                    break
                visit.append(n)
                stk += set(graph[n]) - set(visit)
    return cnt

def dfs2(stk,cnt,graph,point)


node, line = map(int,sys.stdin.readline().split())
nodes = list(range(1,node+1))
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

ans = []
for i in nodes:
    tmp = list(set(nodes) - set([i]))
    ans.append(dfs(graph,i,tmp))

print(ans)