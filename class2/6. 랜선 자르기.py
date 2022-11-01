import sys

k, n = map(int,sys.stdin.readline().split())

tmp = []
for i in range(k):
    tmp.append(int(sys.stdin.readline()))

lo = 1
hi = max(tmp)

while lo <= hi:
    mid = (lo + hi) // 2
    lan = 0

    for i in tmp:
        lan += i // mid

    if lan >= n:
        lo = mid + 1
    else:
        hi = mid - 1
print(hi)