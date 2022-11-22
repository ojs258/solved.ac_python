import sys

nums = list(0 for _ in range(0,10001))

for i in range(int(sys.stdin.readline())):
    nums[int(sys.stdin.readline())] += 1

for i in range(len(nums)):
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i)