import sys
#n개 중에 k개를 고르는 경우의 수 
n, k = map(int,sys.stdin.readline().split())
ans = 1; tmp = 1
for i in range(0,k):
    ans *= n-i
    tmp *= i+1

print(ans//tmp)