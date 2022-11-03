import sys

num = list(int(sys.stdin.readline())
for i in range(int(sys.stdin.readline())))

num1 = sorted(set(num))
num2 = []
print(sum(num) / len(num))
print(num1[len(num1)//2])

for i in len(num1):
    num2[i] = [num1[i]]

print(num2[])

print(abs(max(num) - min(num)))