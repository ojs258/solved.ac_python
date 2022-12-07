import sys

tar_ch = int(sys.stdin.readline()); subin = 100
ans = abs(subin - tar_ch)
e_cnt = int(sys.stdin.readline())
if e_cnt : #고장난 버튼이 존재할 경우
    e_btn = set(sys.stdin.readline().split())
else:
    e_btn = set()

for i in range(1000001):
    for n in str(i):
        if n in e_btn:
            break
    else:
        ans = min(ans,len(str(i)) + abs(i - tar_ch))
print(ans)