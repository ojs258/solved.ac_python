import sys

for _ in range(int(sys.stdin.readline())):
    tmp = []
    for i in sys.stdin.readline().rstrip('\n'):
        if i == '(':
            tmp.append('(')
        elif i == ')':
            if len(tmp) != 0 and tmp[-1] == '(':
                tmp.pop()
            else:
                tmp.append('F')
                break
    if len(tmp) == 0:
        print('YES')
    else:
        print('NO')