import sys

from numpy import sort

tmp = []
for i in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().rstrip('\n')
    tmp.append([len(a),a])

set(tmp)
print(sorted(tmp, key= lambda x:(x[0], x[1])))