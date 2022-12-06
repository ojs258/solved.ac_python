import sys
from itertools import product # 중복 순열을 만들어주는 모듈
# ex) 1111 1112 1113 1114 1121 1122 1123... n
chnl = int(sys.stdin.readline())
e_cnt = int(sys.stdin.readline())
btn = list(range(0,10)) # 고장나지 않은 리모콘의 버튼리스트
chlen = len(list(str(chnl)))
if e_cnt != 0: #고장난 버튼이 존재할 경우
    e_btn = list(map(int,sys.stdin.readline().split()))
    for i in e_btn:
        btn.remove(i) # 고장난 버튼은 버튼 리스트에서 제거
subin = 100
tmp2 = []
tmp = list(product(btn, repeat= chlen))
hap = 0

# 중복 순열이 리스트 형태이므로 각 자리에
# 10의 제곱꼴을 곱해서 숫자로 만들어줌
for i in tmp:
    for j in range(0,chlen):
        hap += i[chlen - (j+1)]*(10**j)
    tmp2.append(hap)
    hap = 0
tmp3 = {}

for i in tmp2:
    tmp3[abs(chnl - i)] = i

samech = tmp3.get(min(tmp3))
if chnl == subin:
    print(0)
else:
    print(len(list(str(samech))) + min(tmp3))