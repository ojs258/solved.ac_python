import sys

n = int(sys.stdin.readline())
cnt = 0
flo = 1
while True:
    flo = flo + cnt * 6
    cnt += 1
    if n <= flo:
        print(cnt)
        break