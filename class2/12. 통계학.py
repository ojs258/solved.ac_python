import sys
from collections import Counter

num = list(int(sys.stdin.readline())
for i in range(int(sys.stdin.readline())))

num.sort()
c_num = Counter(num).most_common()

#평균값
print(int(round(sum(num) / len(num),0)))
#중앙값
print(sorted(num)[len(num)//2])
#최빈값
if len(c_num) > 1:
        if c_num[0][1] == c_num[1][1]:
            print(c_num[1][0])
        else:
            print(c_num[0][0])
else:
    print(c_num[0][0])
#범위
print(max(num)-min(num))