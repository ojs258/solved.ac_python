import sys

stack_size = int(sys.stdin.readline())

num = [int(sys.stdin.readline())
for _ in range(stack_size)]

stack = []; ans = []; push_key = 1; pop_key = 0; cond = 1

while pop_key < stack_size:
    while push_key <= num[pop_key]:
        stack.append(push_key)
        ans.append('+')
        push_key += 1
 
    if stack[-1] == num[pop_key]:
        pop_key += 1
        stack.pop()
        ans.append('-')
    else:
        print("NO")
        cond = 0
        break

if cond == 1:
    for i in ans:
        print(i)