import sys
num = []
for i in range(10):
    num.append(int(sys.stdin.readline())%42)
print(len(set(num)))
