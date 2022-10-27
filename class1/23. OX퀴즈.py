ans=[]
score = 0
cnt = 0
for i in range(int(input())):
    OX = list(input())
    for x in OX:
        if x == 'O':
            cnt = cnt + 1
            score = score + cnt
        else:
            cnt = 0
    ans.append(score)
    cnt = 0
    score = 0
for i in ans:
    print(i, end='\n')
