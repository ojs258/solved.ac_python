import sys, math





a, b = map(int, sys.stdin.readline().split())
while True:
    tmp = a % b
    if tmp == 0:
        print(b)
    else:
        a = b
        b = tmp
    

#print(math.gcd(a,b), math.lcm(a,b), sep="\n")