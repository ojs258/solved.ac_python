import sys
n, m = map(int,sys.stdin.readline().split())

tmp = []
cnt = []
for _ in range(n):
    tmp.append(list(sys.stdin.readline().rstrip('\n')))

for z in range(m-7):
    for y in range(n-7):
        w_cnt = 0
        b_cnt = 0
        for x in range(z, z+8):
            for w in range(y, y+8):
                if (x+w) % 2 == 0:
                    if tmp[w][x] != 'W':
                        w_cnt += 1
                    else:
                        b_cnt += 1
                else:
                    if tmp[w][x] != 'B':
                        w_cnt += 1
                    else:
                        b_cnt += 1
        cnt.append(w_cnt)
        cnt.append(b_cnt)
print(min(cnt))