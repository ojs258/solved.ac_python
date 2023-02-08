import sys
from collections import deque

def bfs():
    que = deque([n])
    while que:
        x = que.popleft()
        if x == k:
            print(t_arr[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= MAX and not t_arr[i]:
                t_arr[i] = t_arr[x] + 1
                que.append(i)
        
n, k = map(int, sys.stdin.readline().split())
MAX = 10 ** 5
t_arr = [0] * (MAX + 1)

bfs()