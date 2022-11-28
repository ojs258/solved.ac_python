import sys, math

n, m, b = map(int,sys.stdin.readline().split())

dirt = []
ans = sys.maxsize
flo = 0
for i in range(n):
    for j in map(int,sys.stdin.readline().split()):
        dirt.append(j)

for tg in range(257):
    maxt = 0; mint = 0
    
    for i in dirt:
        if i >= tg:
            maxt += i - tg
        else:
            mint += tg - i
        
    if maxt + b >= mint:
        if mint + (maxt * 2) <= ans:
            ans = mint + (maxt * 2)
            flo = tg
print(ans,flo)