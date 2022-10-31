import sys

while True:
    num = list(sys.stdin.readline().rstrip('\n'))

    if num == ['0']:
        break
    elif num == list(reversed(num)):
        print('yes')
    else:
        print('no')