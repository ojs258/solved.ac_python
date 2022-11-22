import sys

n, k = map(int,sys.stdin.readline().split())

nums = list(range(1,n+1))
ans = []
cnt = 0
while len(nums) > 0:
    cnt += k-1
    
    if cnt >= len(nums):
        cnt = cnt % len(nums)

    ans.append(str(nums[cnt]))
    nums.remove(nums[cnt])

print('<',', '.join(ans),'>',sep='')
