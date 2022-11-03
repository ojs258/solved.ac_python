import sys

m, n = map(int,sys.stdin.readline().split())

def prm(i):
    if i == 1:
        pass
    else:
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                return False
        return True

for i in range(m,n+1):
    if prm(i):
        print(i)