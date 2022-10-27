import sys
num = []
mul = 1
for i in range(3):
    num.append(int(sys.stdin.readline()))
for i in range(3):
    mul *= num[i]
nums = str(mul)
for i in range(10):
    print(nums.count(str(i)))