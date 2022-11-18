import sys
ans = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    if n != 0:
        ans.append(n)
    else:
        ans.pop()
print(sum(ans))