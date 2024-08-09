n, k = map(int, input().split())
number = list(map(int, input()))
stack = []

for i in number:
    while stack and i > stack[-1] and k > 0:
        stack.pop()
        k -= 1

    stack.append(i)

if k == 0:
    print(*stack, sep = '')
else:
    print(*stack[:-k], sep = '')
