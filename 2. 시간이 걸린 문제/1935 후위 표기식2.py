# 후위 표기식
# 1 2 3 * + 4 5 / -
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 6] (*)
# [7] (+)
# [7, 4]
# [7, 4, 5]
# [7, 0.8] (/)
# [6.2] (-)

n = int(input())
a = list(input())
value = [int(input()) for _ in range(n)]
stack = []
result = 0

for i in a:
    if 'A' <= i <= 'Z':
        stack.append(value[ord(i) - 65])
    else:
        y = stack.pop()
        x = stack.pop()
        if i == '+':
            stack.append(x + y)
        elif i == '-':
            stack.append(x - y)
        elif i == '*':
            stack.append(x * y)
        elif i == '/':
            stack.append(x / y)

print(f"{stack[0]:.2f}")
