import sys

sys.stdin.readline()
sen = list(map(str,sys.stdin.readline().rstrip('\n')))
tmp = []

for i in range(len(sen)):
    tmp.append((ord(sen[i])-96) * (31 ** i))

print(sum(tmp) % 1234567891)