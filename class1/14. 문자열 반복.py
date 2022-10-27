ans = []
cnt = int(input())
for i in range(cnt):
    sentence = []
    a, b = map(str,input().split())
    for i in b:
        for x in range(int(a)):
            sentence.append(i)
    ans.append(sentence)
for i in ans:
    for x in range(len(i)):
        print(i[x], end='')
    print()