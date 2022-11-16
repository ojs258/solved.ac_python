
import sys

while True:
    sen = list(sys.stdin.readline().rstrip('\n'))
    tmp = []
    cond = True
    if sen[0] == '.':
        break

    for i in sen:
        if i == '(' or i == '[':
            tmp.append(i)
        elif i == ')':
            if len(tmp) != 0 and tmp[-1]== '(':
                tmp.pop()
            else:
                tmp.append('F')
                break
        elif i == ']':
            if len(tmp) != 0 and tmp[-1]== '[':
                tmp.pop()
            else:
                tmp.append('F')
                break
    if len(tmp) == 0:
        print('yes')
    else:
        print('no')
