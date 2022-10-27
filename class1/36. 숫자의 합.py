import sys
sys.stdin.readline()
hap = 0
num = list(sys.stdin.readline().rstrip('\n'))
for i in num:
    hap += int(i)
print(hap)