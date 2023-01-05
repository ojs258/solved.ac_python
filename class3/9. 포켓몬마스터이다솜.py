import sys

n, m = map(int, sys.stdin.readline().split())
dic1 = {}; dic2 = {}
for i in range(1,n+1):
    tmp = str(sys.stdin.readline().rstrip('\n'))
    dic1[i] = tmp
    dic2[tmp] = i

for i in range(m):
    search = sys.stdin.readline().rstrip('\n')
    if search.isdigit():
        print(dic1.get(int(search)))
    else:
        print(dic2.get(search))