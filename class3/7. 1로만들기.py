import sys

def mo(n):
    ans = [0] * (n + 1)
    for i in range(2, n + 1):
        ans[i] = ans[i-1] + 1
# 이전 값보다 1증가하였기 때문에 지금 값에 -1을 했을때의 경우의 수
        if i % 2 == 0:
            ans[i] = min(ans[i], ans[i // 2] + 1)
# 지금 값이 2로 나누어 진다면
# 지금 값을 2로 나누었을때의 숫자의 횟수 + 1회(2로 나눈다 한번) 
        if i % 3 == 0:
            ans[i] = min(ans[i], ans[i // 3] + 1)
# 지금 값이 3으로 나누어 진다면
# 지금 값을 3으로 나누었을때의 숫자의 횟수 + 1회(3으로 나눈다 한번)
    return ans[n]
num = int(sys.stdin.readline())
print(mo(num))