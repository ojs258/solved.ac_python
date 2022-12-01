import sys

N, r, c = map(int,sys.stdin.readline().split())

dx=[1,-1,1,-1]
dy=[0,1,0,-1]
a, b = 0, 0
cnt = 0
while cnt < 2**(2*N):
    for i in range(4):
        a += dx[i]; b += dy[i]
        if a == c and b == 
        cnt += 1
