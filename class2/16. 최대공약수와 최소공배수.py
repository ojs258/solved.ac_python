import sys#, math
a, b = map(int, sys.stdin.readline().split())
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcm(x,y):
    return (x * y) // gcd(x,y)

print(gcd(a,b), lcm(a,b),sep='\n')

#print(math.gcd(a,b), math.lcm(a,b), sep="\n")