import sys

tmp = []
words = []
for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().rstrip('\n')
    tmp.append(a)

tmp = list(set(tmp))

for i in tmp:
    words.append([i,len(i)])

for i in sorted(words, key= lambda x: (x[1], x[0])):
    print(i[0])