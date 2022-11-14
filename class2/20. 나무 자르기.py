import sys

n, m = map(int,sys.stdin.readline().split())

tree = list(map(int,sys.stdin.readline().split()))

lo = 1; hi = max(tree)

while lo <= hi:
    mid = (lo + hi) // 2

    ltree = 0
    for i in tree:
        if i > mid:
            ltree += i - mid

    if ltree >= m:
        lo = mid + 1
    else:
        hi = mid - 1
print(hi)