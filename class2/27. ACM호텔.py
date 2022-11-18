import sys

for _ in range(int(sys.stdin.readline())):
    h, w, n = map(int,sys.stdin.readline().split())

    flo = n % h * 100
    room = n // h

    if flo == 0:
        print(h * 100 + room)
    else:
        print(flo + room + 1)