import sys

while True:
    sen = list(sys.stdin.readline())
    tmp = []
    cond = True
    if sen == ['.']:
        break

    for i in sen:
        if i == '(':
            tmp.append(i)
        elif i == ')':
            