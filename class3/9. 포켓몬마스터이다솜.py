import sys

n, m = map(int, sys.stdin.readline().split())
dic1 = {}; dic2 = {}
for i in range(1,n+1):
    tmp = str(sys.stdin.readline().rstrip('\n'))
    dic1[i] = tmp
    dic2[tmp] = i

for i in range(m):
    tmp = sys.stdin.readline()
    if tmp.isdigit():
        print(dic1.get(int(tmp)))
    else:
        print(dic2.get(tmp))