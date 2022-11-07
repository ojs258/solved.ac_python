import sys

n = int(sys.stdin.readline())
for i in range(0,19):
    a = 2**i
    b = 2**(i+1)

    if n&(n-1) == 0:
        print(n)
        break
    else:
        if a <= n and n < b:
            print(n-(b-n))
            break