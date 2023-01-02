import sys

def thr(n):
    return n // 3
def two(n):
    return n // 2
def one(n):
    return n - 1

num = int(sys.stdin.readline())
if num % 3 == 0:
    num //= 3
else:
    if (num - 1) % 3 == 0:
        num -= 1
