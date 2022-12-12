import sys

def dfs(graph, root):
    visit = []
    stk = [root]

    while stk:
        n = stk.pop()
        if n not in visit:
            visit.append(n)
            tmp = sorted(set(graph[n]) - set(visit), reverse= True)
            stk += tmp
    return visit

def bfs(graph, root):
    visit = []
    stk = [root]

    while stk:
        n = stk.pop(0)
        if n not in visit:
            visit.append(n)
            stk += set(graph[n]) - set(visit)
    return visit

point, line, start = map(int,sys.stdin.readline().split())

line_info = list(list(map(int,sys.stdin.readline().split()))
for _ in range(line))

line_info = sorted(line_info)
tmp = []
graph = {}
for i in range(1,1001):
    for j in range(line):
        if i == line_info[j][0]:
            tmp.append(line_info[j][1])
        elif i == line_info[j][1]:
            tmp.append(line_info[j][0])
    if tmp:
        graph[i] = set(tmp)
    tmp = []

for i in dfs(graph,start):
    print(i,end=" ")
print()
for i in bfs(graph,start):
    print(i,end=" ")