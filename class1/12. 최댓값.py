import sys

num={}
for i in range(1,10):
    num[(int(sys.stdin.readline()))] = i

print(max(num), num.get(max(num)), sep='\n')