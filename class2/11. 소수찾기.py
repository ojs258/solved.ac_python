import sys

def prm(i):
    if i == 1:
        pass
    else:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                return False
        return True
input()
num = list(map(int,sys.stdin.readline().split()))
cnt = 0
for i in num:
    if prm(i):
        cnt += 1
print(cnt)