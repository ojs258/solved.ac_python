import sys
sys.stdin.readline()
n = set((map(int,sys.stdin.readline().split())))
sys.stdin.readline()
m = map(int,sys.stdin.readline().split())

for i in m:
    print(1) if i in n else print(0)