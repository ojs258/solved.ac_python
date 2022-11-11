import sys

n, m = map(int,sys.stdin.readline().split())

card = sorted(list(map(int,sys.stdin.readline().split())))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            hap = card[i]+card[j]+card[k]
            if m < hap:
                continue
            else:
                ans = max([ans,hap])
print(ans)
