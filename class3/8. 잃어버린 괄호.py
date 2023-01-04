import sys

tmp = []
a = list(map(str, sys.stdin.readline().rstrip('\n').split('-')))

for i in a:
    tmp.append(sum(list(map(int, i.split('+')))))
ans = tmp[0]
for i in range(1,len(tmp)):
    ans -= tmp[i]

print(ans)
