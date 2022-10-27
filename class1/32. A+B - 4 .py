import sys

while True:
    a = sys.stdin.readline()
    if not a:
        break
    print(sum(map(int,a.split())))