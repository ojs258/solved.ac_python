import sys

sca = []
for i in range(8):
    sca.append(i+1)

inp = list(map(int,sys.stdin.readline().rstrip('\n').split()))

if sca == inp:
    print('ascending')
elif list(reversed(sca)) == inp:
    print('descending')
else:
    print('mixed')