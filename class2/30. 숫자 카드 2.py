import sys, collections
sys.stdin.readline()
nums = list(map(int,sys.stdin.readline().split()))

sys.stdin.readline()
fnum = list(map(int,sys.stdin.readline().split()))

ans = collections.Counter(nums)

for i in fnum:
    print(ans[i], end=' ')