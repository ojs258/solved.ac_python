import sys

dchi = []

for i in range(int(sys.stdin.readline())):
    
    dchi.append(list(map(int,sys.stdin.readline().split())))

for i in dchi:
    rank = 1
    for j in dchi:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank,end=' ')

# 두 종류의 값이 전부 커야 순위 변동이 생김
# 두 가지 값이 전부 1 이어야 1이나오는 논리곱(AND)과 유사\
# 1. AND 생각을 못함, 2. 서로 같은 값을 비교하면 안된다고 생각함.
# 일단 복잡도를 생각하지 않고 짜고 천천히 생각해보기