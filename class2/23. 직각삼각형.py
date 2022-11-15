import sys

while True:
    nums = list(map(float, sys.stdin.readline().split()))

    numax = max(nums)
    nums.remove(numax)
    if sum(nums) == 0:
        break
    elif nums[0]**2 + nums[1]**2 == numax**2:
        print('right')
    else:
        print('wrong')
# 입력 부분에 여러가지 방식으로 테스트케이스가 입력된다 라고 되어있고
# a, b, c가 각각 높이 밑변 빗변의 값이 들어온다고 명시 되어있지않다.
# 고로 리스트로 값을 받아 가장 큰값을 빗변으로 두고 계산해야한다.