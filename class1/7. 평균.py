import sys
input()

grade = list(map(int,sys.stdin.readline().rstrip('\n').split()))

c_grade = []
for i in grade:
    c_grade.append(i / max(grade) * 100)
print(sum(c_grade)/len(grade))