import sys

x, y, w, h = list(map(int,sys.stdin.readline().split()))

print(min([w-x, h-y, x, y]))