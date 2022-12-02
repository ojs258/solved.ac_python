import sys

dx=[0,1,0,1]
dy=[0,0,1,1]

n, y, x = map(int,sys.stdin.readline().split())
ans = 0
while n > 1:
    n -= 1
    size = 2 ** n
    if x < size and y < size:#2사분면
        pass
    elif x < size and y >= size:#3사분면
        ans += (size ** 2) * 2
        y -= size
    elif x >= size and y < size:#1사분면
        ans += size ** 2
        x -= size
    elif x >= size and y >= size:#4사분면
        ans += (size ** 2) * 3
        x -= size; y -= size

for i in range(4):
    if x == dx[i] and y == dy[i]:
        ans += i

print(ans)