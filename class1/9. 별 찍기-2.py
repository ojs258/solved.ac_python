n = int(input())
for i in range(1, n+1):
    for x in range(n-i):
        print(' ', end='')
    for z in range(i):
        print('*', end='')
    print()