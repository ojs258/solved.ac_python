import sys

pos = []

for _ in range(int(sys.stdin.readline())):
    x, y = map(int,sys.stdin.readline().split())

    pos.append([x,y])

ans = list(sorted(pos,key= lambda x:(x[0],x[1])))

for i in ans:
    for j in range(2):
        print(i[j],end=' ')
    print()