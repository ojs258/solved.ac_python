import sys

#백준 채점서버의 최대 재귀함수 깊이는 1000번이다.
sys.setrecursionlimit(10**6)
#sys 모듈의 재귀깊이 설정함수를 통해 재귀깊이 제한을 풀어준다.

# [0,1], [0,-1], [-1,0], [1,0] 각각 상 하 좌 우 십자방향
dx = [0,0,-1,1]
dy = [1,-1,0,0]
ans = 0
def bfs(i,j):
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
# 밭의 최대크기를 넘어가지 않도록 해줌
        if 0 <= x < m and 0 <= y < n:
# 인접한 칸에 배추가 심어져있다면 기준을 인접한 칸으로 바꾸고 검사
            if field[y][x] == 1:
                field[y][x] = 0
                bfs(x,y)


for _ in range(int(sys.stdin.readline())):
    m, n, k = map(int,sys.stdin.readline().split())
    field = [[0]*m for _ in range(n)]
    ans = 0

    for _ in range(k):
        a, b = map(int,sys.stdin.readline().split())
        field[b][a] = 1

    for i in range(m):
        for j in range(n):
            if field[j][i] == 1:
                ans += 1
                bfs(i,j)
    print(ans)
