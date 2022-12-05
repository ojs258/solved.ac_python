import sys

chnl = int(sys.stdin.readline())
e_cnt = int(sys.stdin.readline())
e_btn = list(map(int,sys.stdin.readline().split()))
btn = list(range(0,9))
for i in e_btn:
    btn.remove(i)
subin = 100



if chnl > subin:
    

elif chnl == subin:
    print(0)
else:
    print(subin)
