import sys

n = int(sys.stdin.readline())
paper = []
check = [-1, 0, 1]
ans=[0,0,0]
tmp = []
for i in range(n):
    paper.append(list(map(str,sys.stdin.readline().rstrip('\n').split())))

while n != 0:
    cnt = (n**(1/2))*3
    for i in range(0,n,cnt):
        for j in range(0,n,cnt):
            tmp.append(paper[j:j+cnt])
    for i in check:
        if paper.count(i) == 3 ** cnt:
            ans[i] += 1

print(ans)

