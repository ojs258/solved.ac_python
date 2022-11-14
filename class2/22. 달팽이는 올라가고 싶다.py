import sys

a, b, v = map(int, sys.stdin.readline().split())

snail = 0; day = 0
while True:
    snail += a
    day += 1
    if v <= snail:
        print(day)
        break
    snail -= b